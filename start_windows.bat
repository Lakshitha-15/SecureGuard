@echo off
echo ========================================
echo    SecureGuard - Quick Start Script
echo ========================================
echo.

echo Step 1: Installing Python dependencies...
cd backend
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Failed to install dependencies
    echo Please make sure Python and pip are installed
    pause
    exit /b 1
)

echo.
echo Step 2: Starting Flask backend...
echo.
echo Backend will run on http://localhost:5000
echo.
echo After backend starts, open frontend/index.html in your browser
echo.
echo Press Ctrl+C to stop the server
echo.
python app.py

pause
