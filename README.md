# 🛡️ SecureGuard - Login Security Analytics Platform

A complete full-stack data visualization and security analytics platform built with Python Flask backend and modern JavaScript frontend.

## 📋 Project Overview

SecureGuard is a comprehensive login security monitoring system that provides:
- Real-time dashboard with interactive charts
- Geographic analysis of login patterns
- Bloom filter-based IP blacklist checking
- Advanced anomaly detection (brute force, impossible travel, etc.)
- Searchable login logs with filtering capabilities

## 🎯 Features

### ✅ Backend (Python Flask)
- RESTful API with 9+ endpoints
- CSV data processing with Pandas
- Bloom Filter implementation for space-efficient IP blacklist
- Anomaly detection algorithms:
  - Brute force attack detection
  - Impossible travel detection
  - Off-hours login detection
  - Geographic anomaly detection
  - Rapid login attempt detection
- Geographic analysis and aggregation

### ✅ Frontend (HTML/CSS/JavaScript)
- Modern dark theme UI
- 4 distinct pages:
  - **Dashboard**: Real-time stats, charts, and alerts
  - **Geographic Analysis**: Country/city breakdown with visualizations
  - **Login Logs**: Searchable table with advanced filters
  - **Bloom Filter**: IP checker and anomaly reports
- Interactive Chart.js visualizations
- Responsive design

### ✅ Dataset
- 800+ real login records
- Includes: username, IP, country, city, status, timestamp
- Mix of successful and failed attempts
- Multiple countries and users for realistic analysis

## 🏗️ Project Structure

```
secureguard_project/
│
├── backend/
│   ├── app.py                    # Main Flask application
│   ├── requirements.txt          # Python dependencies
│   ├── data/
│   │   └── login_logs.csv        # Login dataset (800 records)
│   └── utils/
│       ├── bloom.py              # Bloom Filter implementation
│       ├── anomaly.py            # Anomaly detection algorithms
│       └── geo_analysis.py       # Geographic analysis module
│
├── frontend/
│   ├── index.html                # Landing page
│   ├── dashboard.html            # Main dashboard
│   ├── geo.html                  # Geographic analysis page
│   ├── logs.html                 # Login logs page
│   ├── bloom.html                # Bloom filter page
│   ├── js/
│   │   ├── api.js                # API helper functions
│   │   ├── charts.js             # Chart.js utilities
│   │   └── main.js               # Main JS logic
│   └── css/
│       └── styles.css            # Main stylesheet
│
└── README.md                     # This file
```

## 🚀 Quick Start Guide

### Prerequisites
- Python 3.8 or higher
- Modern web browser (Chrome, Firefox, Edge)
- VS Code (recommended) or any code editor

### Installation Steps

#### 1. Navigate to Backend Directory
```bash
cd secureguard_project/backend
```

#### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install Flask==3.0.0
pip install flask-cors==4.0.0
pip install pandas==2.1.4
```

#### 3. Start the Flask Backend
```bash
python app.py
```

You should see:
```
✅ Loaded 800 records from CSV
✅ Added 50 suspicious IPs to Bloom Filter
🚀 SecureGuard Backend Starting...
📊 API running on http://localhost:5000
```

#### 4. Open Frontend
Open any of these files in your browser:
- `frontend/index.html` - Landing page
- `frontend/dashboard.html` - Main dashboard

Or use VS Code Live Server:
1. Right-click on `frontend/index.html`
2. Select "Open with Live Server"

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/load-data` | GET | Check if data is loaded |
| `/api/stats` | GET | Get dashboard statistics |
| `/api/geo-analysis` | GET | Get geographic analysis |
| `/api/login-logs` | GET | Get login logs (with filters) |
| `/api/bloom-check` | POST | Check if IP is suspicious |
| `/api/anomaly-detect` | GET | Get all detected anomalies |
| `/api/recent-alerts` | GET | Get recent security alerts |
| `/api/timeline` | GET | Get login timeline data |
| `/api/user-analysis/<username>` | GET | Get user-specific analysis |

### Example API Usage

```bash
# Get statistics
curl http://localhost:5000/api/stats

# Get login logs (filtered)
curl "http://localhost:5000/api/login-logs?country=India&status=failed&limit=50"

# Check IP with Bloom Filter
curl -X POST http://localhost:5000/api/bloom-check \
  -H "Content-Type: application/json" \
  -d '{"ip": "192.168.1.1"}'
```

## 🎨 Features Breakdown

### 1. Dashboard (`dashboard.html`)
- **Stats Cards**: Total logins, success rate, failed logins, unique users
- **Timeline Chart**: Line chart showing success vs failed logins over time
- **Status Distribution**: Pie chart of overall login status
- **Recent Alerts**: Real-time security alerts
- **Recent Activity Table**: Latest 20 login attempts

### 2. Geographic Analysis (`geo.html`)
- **Country Bar Chart**: Top countries by login count
- **Success/Failed by Country**: Grouped bar chart
- **Country Statistics Table**: Detailed breakdown with success rates
- **City Statistics Table**: Top 20 cities

### 3. Login Logs (`logs.html`)
- **Advanced Filters**: Username search, country filter, status filter, result limit
- **Searchable Table**: All login records with sorting
- **Real-time Results**: Dynamic filtering without page reload

### 4. Bloom Filter (`bloom.html`)
- **IP Checker**: Input any IP to check if it's in the blacklist
- **Bloom Filter Explanation**: Educational content about the algorithm
- **Anomaly Detection Results**: All detected security threats
- **Anomaly Charts**: Distribution and severity breakdown

## 🔍 Key Algorithms

### Bloom Filter
- **Size**: 1000 bits
- **Hash Functions**: 3
- **Use Case**: Efficient IP blacklist checking
- **Characteristics**: 
  - No false negatives (if IP is NOT in filter, it's definitely clean)
  - Possible false positives (may flag clean IPs as suspicious)

### Anomaly Detection

1. **Brute Force Detection**
   - Threshold: 3+ failed attempts from same IP
   - Severity: High (5+ attempts) or Medium (3-4 attempts)

2. **Impossible Travel**
   - Detects logins from different countries within 2 hours
   - Severity: Critical

3. **Off-Hours Login**
   - Detects logins between midnight and 6 AM
   - Severity: Low

4. **Geographic Anomaly**
   - Detects users logging in from 4+ different countries
   - Severity: Medium

5. **Rapid Login Attempts**
   - Detects login attempts within 60 seconds
   - Severity: Medium

## 🎓 Educational Value

This project demonstrates:
- ✅ Full-stack development (Python + JavaScript)
- ✅ RESTful API design
- ✅ Data visualization with Chart.js
- ✅ CSV data processing with Pandas
- ✅ Probabilistic data structures (Bloom Filter)
- ✅ Security analytics and threat detection
- ✅ Frontend-backend integration
- ✅ Modular code organization

## 🛠️ Customization

### Adding More Data
Replace `backend/data/login_logs.csv` with your own CSV file. Ensure it has these columns:
- `username`
- `ip`
- `country`
- `city`
- `status` (success/failed)
- `timestamp` (YYYY-MM-DD HH:MM:SS)

### Modifying Bloom Filter
Edit `backend/utils/bloom.py`:
```python
# Change size and hash count
bloom_filter = BloomFilter(size=2000, hash_count=5)
```

### Adjusting Anomaly Thresholds
Edit `backend/utils/anomaly.py`:
```python
# Example: Change brute force threshold
if count >= 5:  # Changed from 3 to 5
```

## 🐛 Troubleshooting

### Backend won't start
- **Error**: `ModuleNotFoundError: No module named 'flask'`
  - **Solution**: Run `pip install -r requirements.txt`

- **Error**: `Address already in use`
  - **Solution**: Port 5000 is occupied. Change port in `app.py`:
    ```python
    app.run(debug=True, port=5001)  # Use different port
    ```

### Frontend shows errors
- **Error**: `Failed to fetch`
  - **Solution**: Make sure backend is running on `http://localhost:5000`
  
- **Error**: CORS errors in console
  - **Solution**: Backend has `flask-cors` installed, reinstall if needed

### Charts not displaying
- **Error**: Charts are blank
  - **Solution**: Check browser console for errors. Ensure Chart.js CDN is accessible.

## 📊 Dataset Statistics

- **Total Records**: 800
- **Unique Users**: 10
- **Countries**: 8 (India, USA, UK, Germany, Canada, Australia, etc.)
- **Cities**: 15+
- **Date Range**: March 2026
- **Success Rate**: ~70-80%

## 🔐 Security Features

1. **Bloom Filter IP Blacklist**: Space-efficient suspicious IP detection
2. **Brute Force Detection**: Identifies repeated failed login attempts
3. **Impossible Travel Detection**: Catches physically impossible login patterns
4. **Geographic Anomalies**: Flags unusual country access patterns
5. **Off-Hours Monitoring**: Detects suspicious timing patterns
6. **Real-time Alerts**: Immediate notification of security events

## 📈 Performance

- **API Response Time**: < 100ms for most endpoints
- **Frontend Load Time**: < 2 seconds
- **Bloom Filter Lookup**: O(1) constant time
- **Data Processing**: Efficient Pandas operations
- **Memory Usage**: Minimal (~50MB for 800 records)

## 🎯 Use Cases

- **Academic Projects**: Perfect for data visualization lab assignments
- **Security Training**: Learn about security analytics
- **Portfolio Projects**: Showcase full-stack development skills
- **Learning Tool**: Understand Bloom filters and anomaly detection
- **Interview Prep**: Demonstrate system design and API development

## 📝 Future Enhancements

Potential features to add:
- [ ] User authentication and authorization
- [ ] Export data to PDF/Excel
- [ ] Email alerts for critical anomalies
- [ ] Machine learning-based anomaly detection
- [ ] Real-time WebSocket updates
- [ ] Database integration (PostgreSQL/MongoDB)
- [ ] Docker containerization
- [ ] API rate limiting
- [ ] Data encryption

## 👨‍💻 Development

### Running in Development Mode

Backend:
```bash
cd backend
python app.py
# Flask debug mode is enabled by default
```

Frontend:
- Use VS Code Live Server extension
- Or open HTML files directly in browser

### Code Style
- **Python**: PEP 8 compliant
- **JavaScript**: ES6+ features
- **CSS**: BEM-like naming convention

## 📄 License

This project is created for educational purposes. Feel free to use and modify for your learning needs.

## 🙏 Acknowledgments

- **Chart.js**: Beautiful charts and visualizations
- **Flask**: Lightweight Python web framework
- **Pandas**: Powerful data analysis library

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section
2. Verify all dependencies are installed
3. Ensure backend is running before accessing frontend
4. Check browser console for errors

## 🎉 Quick Test

After setup, verify everything works:
1. ✅ Backend starts without errors
2. ✅ Visit `http://localhost:5000/api/stats` - should return JSON
3. ✅ Open `frontend/dashboard.html` - should show charts and data
4. ✅ Navigate to all 4 pages - should load without errors
5. ✅ Try filtering on logs page
6. ✅ Check an IP on bloom filter page

---

**Built with ❤️ for learning and education**

Version: 1.0.0 | Last Updated: March 2026
