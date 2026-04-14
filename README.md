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

### Installation Steps

#### 1. Navigate to Backend Directory
```bash
cd secureguard_project/backend
```

#### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Start the Flask Backend
```bash
python app.py
```

#### 4. Open Frontend
Open any of these files in your browser:
- `frontend/index.html` - Landing page
- `frontend/dashboard.html` - Main dashboard

Or use VS Code Live Server:
1. Right-click on `frontend/index.html`
2. Select "Open with Live Server"

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

## 🔐 Security Features

1. **Bloom Filter IP Blacklist**: Space-efficient suspicious IP detection
2. **Brute Force Detection**: Identifies repeated failed login attempts
3. **Impossible Travel Detection**: Catches physically impossible login patterns
4. **Geographic Anomalies**: Flags unusual country access patterns
5. **Off-Hours Monitoring**: Detects suspicious timing patterns
6. **Real-time Alerts**: Immediate notification of security events

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
