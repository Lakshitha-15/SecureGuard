# 🎯 VS Code Setup Guide for SecureGuard

This guide will help you set up and run SecureGuard in VS Code.

## 📦 Prerequisites

1. **Python 3.8+** installed
   - Check: `python --version` or `python3 --version`
   - Download: https://www.python.org/downloads/

2. **VS Code** installed
   - Download: https://code.visualstudio.com/

3. **VS Code Extensions** (Recommended):
   - Python (by Microsoft)
   - Live Server (by Ritwick Dey)
   - Prettier - Code formatter

## 🚀 Setup Steps

### Step 1: Open Project in VS Code

1. Open VS Code
2. File → Open Folder
3. Select the `secureguard_project` folder
4. Click "Select Folder"

### Step 2: Open Integrated Terminal

- View → Terminal (or press `` Ctrl+` ``)
- This opens a terminal at the bottom of VS Code

### Step 3: Install Python Dependencies

In the terminal, run:

```bash
# Navigate to backend folder
cd backend

# Install dependencies
pip install -r requirements.txt
```

**For Mac/Linux users**, you might need:
```bash
pip3 install -r requirements.txt
```

You should see:
```
Successfully installed Flask-3.0.0 flask-cors-4.0.0 pandas-2.1.4
```

### Step 4: Start the Backend Server

Still in the `backend` folder, run:

```bash
python app.py
```

**For Mac/Linux users**:
```bash
python3 app.py
```

You should see:
```
✅ Loaded 800 records from CSV
✅ Added 50 suspicious IPs to Bloom Filter
🚀 SecureGuard Backend Starting...
📊 API running on http://localhost:5000

📋 Available Endpoints:
  GET  /api/load-data
  GET  /api/stats
  ...

✅ Ready to accept requests!

 * Running on http://127.0.0.1:5000
```

**Important**: Keep this terminal running! Don't close it.

### Step 5: Open Frontend

You have 2 options:

#### Option A: Using Live Server (Recommended)

1. In VS Code Explorer (left sidebar), navigate to `frontend/index.html`
2. Right-click on `index.html`
3. Select "Open with Live Server"
4. Your browser will open automatically

#### Option B: Direct File Opening

1. In VS Code Explorer, navigate to `frontend/index.html`
2. Right-click on `index.html`
3. Select "Reveal in File Explorer" (Windows) or "Reveal in Finder" (Mac)
4. Double-click `index.html` to open in your browser

### Step 6: Navigate the Application

Once the frontend opens:

1. **Landing Page** (`index.html`)
   - Click "Launch Dashboard →"

2. **Dashboard** (`dashboard.html`)
   - View stats cards
   - See charts and recent activity
   - Check security alerts

3. **Geographic Analysis** (`geo.html`)
   - View login patterns by country
   - See city statistics

4. **Login Logs** (`logs.html`)
   - Search and filter logs
   - Try filters: country, status, username

5. **Bloom Filter** (`bloom.html`)
   - Test IP addresses
   - View anomaly detection results

## 🔧 Troubleshooting in VS Code

### Problem: "pip is not recognized"

**Solution**:
1. Make sure Python is installed
2. Add Python to PATH during installation
3. Restart VS Code
4. Try: `python -m pip install -r requirements.txt`

### Problem: "Module not found"

**Solution**:
```bash
# Make sure you're in the backend folder
cd backend

# Reinstall
pip install Flask flask-cors pandas
```

### Problem: Backend shows errors

**Solution**:
1. Check if you're in the `backend` folder: `pwd` (Mac/Linux) or `cd` (Windows)
2. Check if CSV file exists: `ls data/` (Mac/Linux) or `dir data\` (Windows)
3. Restart the backend: Press `Ctrl+C` then run `python app.py` again

### Problem: Frontend shows "Failed to fetch"

**Solution**:
1. Make sure backend is running (check the terminal)
2. Backend should show: "Running on http://127.0.0.1:5000"
3. Try accessing http://localhost:5000/api/stats in your browser
4. Check browser console for errors (F12 → Console tab)

### Problem: Charts not showing

**Solution**:
1. Check internet connection (Chart.js loads from CDN)
2. Check browser console for errors (F12)
3. Try hard refresh: `Ctrl+Shift+R` (Windows) or `Cmd+Shift+R` (Mac)

## 📁 VS Code Workspace Tips

### Recommended Settings

Create `.vscode/settings.json` in project root:

```json
{
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "editor.formatOnSave": true,
  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000
}
```

### Useful Keyboard Shortcuts

- `Ctrl+~` - Toggle terminal
- `Ctrl+Shift+P` - Command palette
- `Ctrl+B` - Toggle sidebar
- `F5` - Start debugging (Python)
- `Ctrl+Shift+F` - Search across files

### Split Terminal View

1. In terminal, click the "+" icon to open new terminal
2. Keep backend running in one terminal
3. Use second terminal for other commands

## 🎯 Quick Test Checklist

After setup, verify:

- [ ] Backend terminal shows "Ready to accept requests"
- [ ] Visit http://localhost:5000/api/stats in browser - returns JSON
- [ ] Frontend index.html opens successfully
- [ ] Dashboard shows charts and data
- [ ] All 4 pages load without errors
- [ ] Filtering works on logs page
- [ ] Bloom filter can check IPs

## 🔄 Restarting the Project

### To Stop:
1. Go to terminal running backend
2. Press `Ctrl+C`

### To Start Again:
1. Open VS Code
2. Open terminal (`` Ctrl+` ``)
3. Navigate to backend: `cd backend`
4. Run: `python app.py`
5. Open `frontend/index.html` in browser

## 💡 Pro Tips

1. **Use Multi-Root Workspace**:
   - File → Add Folder to Workspace
   - Add `backend` and `frontend` as separate roots

2. **Debug Backend**:
   - Click Run → Start Debugging (F5)
   - Select "Python File"
   - Set breakpoints in `app.py`

3. **Extensions to Install**:
   - Python
   - Live Server
   - Prettier
   - ES7+ React/Redux snippets (for future enhancements)

4. **View API Responses**:
   - Install "Thunder Client" or "REST Client" extension
   - Test API endpoints directly in VS Code

## 📚 Next Steps

After successful setup:

1. **Explore the Code**:
   - Read through `backend/app.py`
   - Check `backend/utils/*.py` files
   - Review frontend JavaScript files

2. **Customize**:
   - Modify colors in `frontend/css/styles.css`
   - Add new API endpoints in `backend/app.py`
   - Create additional visualizations

3. **Learn**:
   - Study the Bloom Filter implementation
   - Understand anomaly detection algorithms
   - Explore Chart.js documentation

## 🆘 Getting Help

If stuck:
1. Check browser console (F12 → Console)
2. Check terminal for errors
3. Review the main README.md
4. Verify all prerequisites are installed

---

**Happy Coding! 🚀**

Ready to start? Run `python app.py` in the backend folder!
