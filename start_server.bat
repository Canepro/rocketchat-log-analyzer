@echo off
REM =========================================================================
REM RocketChat Support Dump Analyzer - Server Startup Script
REM =========================================================================
REM 
REM Purpose: Convenience script to start the Flask web server
REM Usage:   Double-click this file or run from command line
REM Output:  Opens Flask server at http://localhost:5000
REM 
REM Requirements:
REM - Python 3.7+ installed and in PATH
REM - Flask and dependencies installed (pip install -r requirements.txt)
REM 
REM Author: RocketChat Support Dump Analyzer Team
REM =========================================================================

echo.
echo ==========================================
echo  RocketChat Support Dump Analyzer v2.1.4
echo ==========================================
echo.
echo Starting Flask web server...
echo.

REM Change to the project directory
cd /d "c:\Users\i\rocketchat_analyzer_py"

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    echo.
    pause
    exit /b 1
)

REM Check if app.py exists
if not exist "app.py" (
    echo ERROR: app.py not found in current directory
    echo Make sure you're running this from the project root
    echo Current directory: %cd%
    echo.
    pause
    exit /b 1
)

REM Display startup information
echo Python version:
python --version
echo.
echo Project directory: %cd%
echo Server will start at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo ==========================================
echo.

REM Start the Flask application
python app.py

REM Keep window open if there's an error
echo.
echo ==========================================
echo Server stopped or encountered an error
echo ==========================================
pause
