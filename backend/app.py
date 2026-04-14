from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from datetime import datetime, timedelta
from collections import Counter
import os
from utils.bloom import BloomFilter
from utils.anomaly import AnomalyDetector
from utils.geo_analysis import GeoAnalyzer

app = Flask(__name__)
CORS(app)

# Global variables
df = None
bloom_filter = None
anomaly_detector = None
geo_analyzer = None

def load_data():
    """Load CSV data on startup"""
    global df, bloom_filter, anomaly_detector, geo_analyzer
    
    csv_path = os.path.join(os.path.dirname(__file__), 'data', 'login_logs.csv')
    df = pd.read_csv(csv_path)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    # Initialize components
    bloom_filter = BloomFilter(size=1000, hash_count=3)
    anomaly_detector = AnomalyDetector(df)
    geo_analyzer = GeoAnalyzer(df)
    
    # Add suspicious IPs to bloom filter
    suspicious_ips = df[df['status'] == 'failed']['ip'].unique()
    for ip in suspicious_ips[:50]:  # Add first 50 failed IPs
        bloom_filter.add(ip)
    
    print(f"✅ Loaded {len(df)} records from CSV")
    print(f"✅ Added {len(suspicious_ips[:50])} suspicious IPs to Bloom Filter")

@app.route('/api/load-data', methods=['GET'])
def get_load_data():
    """Endpoint to check if data is loaded"""
    if df is not None:
        return jsonify({
            'status': 'success',
            'total_records': len(df),
            'columns': list(df.columns),
            'message': 'Data loaded successfully'
        })
    else:
        return jsonify({'status': 'error', 'message': 'Data not loaded'}), 500

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get dashboard statistics"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    total_logins = len(df)
    failed_logins = len(df[df['status'] == 'failed'])
    success_logins = len(df[df['status'] == 'success'])
    unique_users = df['username'].nunique()
    unique_countries = df['country'].nunique()
    
    # Recent activity (last 7 days)
    recent_date = df['timestamp'].max() - timedelta(days=7)
    recent_logins = len(df[df['timestamp'] >= recent_date])
    
    # Top countries
    top_countries = df['country'].value_counts().head(5).to_dict()
    
    # Hourly distribution
    df['hour'] = df['timestamp'].dt.hour
    hourly_dist = df.groupby('hour').size().to_dict()
    
    return jsonify({
        'total_logins': total_logins,
        'failed_logins': failed_logins,
        'success_logins': success_logins,
        'success_rate': round((success_logins / total_logins) * 100, 2),
        'unique_users': unique_users,
        'unique_countries': unique_countries,
        'recent_logins': recent_logins,
        'top_countries': top_countries,
        'hourly_distribution': hourly_dist
    })

@app.route('/api/geo-analysis', methods=['GET'])
def get_geo_analysis():
    """Get geographical analysis data"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    analysis = geo_analyzer.get_analysis()
    return jsonify(analysis)

@app.route('/api/login-logs', methods=['GET'])
def get_login_logs():
    """Get login logs with optional filtering"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    # Get query parameters
    country = request.args.get('country')
    status = request.args.get('status')
    username = request.args.get('username')
    limit = request.args.get('limit', 100, type=int)
    
    # Filter data
    filtered_df = df.copy()
    
    if country:
        filtered_df = filtered_df[filtered_df['country'] == country]
    if status:
        filtered_df = filtered_df[filtered_df['status'] == status]
    if username:
        filtered_df = filtered_df[filtered_df['username'].str.contains(username, case=False)]
    
    # Sort by timestamp descending
    filtered_df = filtered_df.sort_values('timestamp', ascending=False)
    
    # Limit results
    filtered_df = filtered_df.head(limit)
    
    # Convert to JSON-serializable format
    logs = filtered_df.to_dict('records')
    for log in logs:
        log['timestamp'] = log['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
    
    return jsonify({
        'total': len(filtered_df),
        'logs': logs
    })

@app.route('/api/bloom-check', methods=['POST'])
def bloom_check():
    """Check if IP is in bloom filter (potentially suspicious)"""
    if bloom_filter is None:
        return jsonify({'error': 'Bloom filter not initialized'}), 500
    
    data = request.get_json()
    ip = data.get('ip')
    
    if not ip:
        return jsonify({'error': 'IP address required'}), 400
    
    is_suspicious = bloom_filter.check(ip)
    
    # Get actual count from data
    actual_count = len(df[(df['ip'] == ip) & (df['status'] == 'failed')])
    
    return jsonify({
        'ip': ip,
        'is_suspicious': is_suspicious,
        'bloom_result': 'Found in blacklist' if is_suspicious else 'Not in blacklist',
        'actual_failed_attempts': actual_count,
        'note': 'Bloom filter may have false positives but no false negatives'
    })

@app.route('/api/anomaly-detect', methods=['GET'])
def anomaly_detect():
    """Detect anomalies in login data"""
    if anomaly_detector is None:
        return jsonify({'error': 'Anomaly detector not initialized'}), 500
    
    anomalies = anomaly_detector.detect_anomalies()
    return jsonify(anomalies)

@app.route('/api/recent-alerts', methods=['GET'])
def get_recent_alerts():
    """Get recent security alerts"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    alerts = []
    
    # Failed login alerts (last 24 hours)
    recent_date = df['timestamp'].max() - timedelta(hours=24)
    recent_failed = df[(df['timestamp'] >= recent_date) & (df['status'] == 'failed')]
    
    for _, row in recent_failed.head(10).iterrows():
        alerts.append({
            'type': 'Failed Login',
            'severity': 'warning',
            'message': f"Failed login attempt from {row['country']} for user {row['username']}",
            'timestamp': row['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
            'ip': row['ip']
        })
    
    # Multiple failed attempts from same IP
    ip_failed_counts = df[df['status'] == 'failed']['ip'].value_counts()
    for ip, count in ip_failed_counts.head(5).items():
        if count >= 3:
            alerts.append({
                'type': 'Brute Force',
                'severity': 'critical',
                'message': f"IP {ip} has {count} failed login attempts",
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'ip': ip
            })
    
    return jsonify({'alerts': alerts[:15]})

@app.route('/api/timeline', methods=['GET'])
def get_timeline():
    """Get login timeline data for charts"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    # Group by date
    df['date'] = df['timestamp'].dt.date
    timeline = df.groupby(['date', 'status']).size().unstack(fill_value=0)
    
    dates = [str(date) for date in timeline.index]
    success = timeline['success'].tolist() if 'success' in timeline.columns else []
    failed = timeline['failed'].tolist() if 'failed' in timeline.columns else []
    
    return jsonify({
        'dates': dates,
        'success': success,
        'failed': failed
    })

@app.route('/api/user-analysis/<username>', methods=['GET'])
def get_user_analysis(username):
    """Get detailed analysis for a specific user"""
    if df is None:
        return jsonify({'error': 'Data not loaded'}), 500
    
    user_df = df[df['username'] == username]
    
    if len(user_df) == 0:
        return jsonify({'error': 'User not found'}), 404
    
    analysis = {
        'username': username,
        'total_logins': len(user_df),
        'failed_logins': len(user_df[user_df['status'] == 'failed']),
        'success_logins': len(user_df[user_df['status'] == 'success']),
        'countries': user_df['country'].unique().tolist(),
        'cities': user_df['city'].unique().tolist(),
        'unique_ips': user_df['ip'].nunique(),
        'first_login': user_df['timestamp'].min().strftime('%Y-%m-%d %H:%M:%S'),
        'last_login': user_df['timestamp'].max().strftime('%Y-%m-%d %H:%M:%S'),
        'recent_activity': user_df.tail(10).to_dict('records')
    }
    
    # Convert timestamps
    for activity in analysis['recent_activity']:
        activity['timestamp'] = activity['timestamp'].strftime('%Y-%m-%d %H:%M:%S')
    
    return jsonify(analysis)

if __name__ == '__main__':
    load_data()
    print("🚀 SecureGuard Backend Starting...")
    print("📊 API running on http://localhost:5000")
    print("\n📋 Available Endpoints:")
    print("  GET  /api/load-data")
    print("  GET  /api/stats")
    print("  GET  /api/geo-analysis")
    print("  GET  /api/login-logs")
    print("  POST /api/bloom-check")
    print("  GET  /api/anomaly-detect")
    print("  GET  /api/recent-alerts")
    print("  GET  /api/timeline")
    print("  GET  /api/user-analysis/<username>")
    print("\n✅ Ready to accept requests!\n")
    app.run(debug=True, port=5000)
