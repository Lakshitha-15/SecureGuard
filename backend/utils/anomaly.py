import pandas as pd
from datetime import datetime, timedelta
from collections import Counter

class AnomalyDetector:
    """
    Anomaly Detection for login activities
    Detects suspicious patterns like:
    - Brute force attempts
    - Impossible travel
    - Off-hours login
    - Geographic anomalies
    """
    
    def __init__(self, df):
        """Initialize with login data"""
        self.df = df
    
    def detect_brute_force(self):
        """Detect brute force attempts (multiple failed logins from same IP)"""
        failed_df = self.df[self.df['status'] == 'failed']
        ip_counts = failed_df['ip'].value_counts()
        
        brute_force = []
        for ip, count in ip_counts.items():
            if count >= 3:  # Threshold: 3 or more failed attempts
                brute_force.append({
                    'ip': ip,
                    'failed_attempts': int(count),
                    'severity': 'high' if count >= 5 else 'medium',
                    'type': 'Brute Force Attack'
                })
        
        return brute_force[:10]  # Return top 10
    
    def detect_impossible_travel(self):
        """Detect impossible travel (logins from different countries in short time)"""
        impossible_travel = []
        
        # Group by username and sort by timestamp
        for username in self.df['username'].unique():
            user_df = self.df[self.df['username'] == username].sort_values('timestamp')
            
            for i in range(len(user_df) - 1):
                current = user_df.iloc[i]
                next_login = user_df.iloc[i + 1]
                
                # Different countries
                if current['country'] != next_login['country']:
                    time_diff = (next_login['timestamp'] - current['timestamp']).total_seconds() / 3600
                    
                    # Less than 2 hours between logins from different countries
                    if time_diff < 2:
                        impossible_travel.append({
                            'username': username,
                            'from_country': current['country'],
                            'to_country': next_login['country'],
                            'time_difference_hours': round(time_diff, 2),
                            'first_login': current['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
                            'second_login': next_login['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
                            'severity': 'critical',
                            'type': 'Impossible Travel'
                        })
        
        return impossible_travel[:10]
    
    def detect_off_hours_login(self):
        """Detect off-hours logins (midnight to 6 AM)"""
        self.df['hour'] = self.df['timestamp'].dt.hour
        off_hours_df = self.df[(self.df['hour'] >= 0) & (self.df['hour'] < 6)]
        
        off_hours = []
        for _, row in off_hours_df.head(15).iterrows():
            off_hours.append({
                'username': row['username'],
                'timestamp': row['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
                'hour': int(row['hour']),
                'country': row['country'],
                'ip': row['ip'],
                'status': row['status'],
                'severity': 'low',
                'type': 'Off-Hours Login'
            })
        
        return off_hours
    
    def detect_geographic_anomaly(self):
        """Detect users logging from unusual number of countries"""
        geographic_anomalies = []
        
        user_countries = self.df.groupby('username')['country'].nunique()
        
        for username, country_count in user_countries.items():
            if country_count >= 4:  # Threshold: 4 or more different countries
                user_df = self.df[self.df['username'] == username]
                countries = user_df['country'].unique().tolist()
                
                geographic_anomalies.append({
                    'username': username,
                    'country_count': int(country_count),
                    'countries': countries,
                    'total_logins': len(user_df),
                    'severity': 'medium',
                    'type': 'Geographic Anomaly'
                })
        
        return geographic_anomalies[:10]
    
    def detect_rapid_login_attempts(self):
        """Detect rapid successive login attempts (within 1 minute)"""
        rapid_attempts = []
        
        for username in self.df['username'].unique():
            user_df = self.df[self.df['username'] == username].sort_values('timestamp')
            
            for i in range(len(user_df) - 1):
                current = user_df.iloc[i]
                next_login = user_df.iloc[i + 1]
                
                time_diff = (next_login['timestamp'] - current['timestamp']).total_seconds()
                
                if time_diff < 60:  # Less than 1 minute
                    rapid_attempts.append({
                        'username': username,
                        'time_difference_seconds': int(time_diff),
                        'first_attempt': current['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
                        'second_attempt': next_login['timestamp'].strftime('%Y-%m-%d %H:%M:%S'),
                        'severity': 'medium',
                        'type': 'Rapid Login Attempts'
                    })
        
        return rapid_attempts[:10]
    
    def detect_anomalies(self):
        """Run all anomaly detection methods"""
        return {
            'brute_force': self.detect_brute_force(),
            'impossible_travel': self.detect_impossible_travel(),
            'off_hours_login': self.detect_off_hours_login(),
            'geographic_anomaly': self.detect_geographic_anomaly(),
            'rapid_attempts': self.detect_rapid_login_attempts(),
            'summary': {
                'total_anomalies': (
                    len(self.detect_brute_force()) +
                    len(self.detect_impossible_travel()) +
                    len(self.detect_off_hours_login()) +
                    len(self.detect_geographic_anomaly()) +
                    len(self.detect_rapid_login_attempts())
                ),
                'critical_count': len(self.detect_impossible_travel()),
                'high_count': len([x for x in self.detect_brute_force() if x.get('severity') == 'high']),
                'medium_count': len(self.detect_geographic_anomaly())
            }
        }
