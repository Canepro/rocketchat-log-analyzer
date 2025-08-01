# 🚀 Startup Guide - RocketChat Support Dump Analyzer

This guide explains the different ways to start the RocketChat Support Dump Analyzer web application.

## 📁 Available Startup Methods

### 1. Windows Batch Script (Recommended for Windows)
**File:** `start_server.bat`

**Usage:**
- Double-click the file in Windows Explorer
- Or run from Command Prompt: `start_server.bat`

**What it does:**
- Automatically navigates to the project directory
- Checks if Python is installed and accessible
- Validates that required files exist
- Displays helpful startup information
- Starts the Flask web server
- Keeps the window open if errors occur

**Requirements:**
- Windows OS
- Python 3.7+ installed and in PATH
- All dependencies installed (`pip install -r requirements.txt`)

### 2. Manual Python Command
**Usage:**
```bash
cd /path/to/rocketchat_analyzer_py
python app.py
```

**When to use:**
- Linux/macOS systems
- When you want direct control over the startup process
- For debugging startup issues

### 3. Docker/Podman (Production)
**Usage:**
```bash
# Build the container
docker build -t rocketchat-analyzer .

# Run the container
docker run -p 5000:5000 rocketchat-analyzer
```

## 🌐 Accessing the Application

Once started, the web application will be available at:
- **Local access:** http://localhost:5000
- **Network access:** http://your-ip-address:5000

## 🔧 Troubleshooting

### Common Issues:

**"Python is not installed or not in PATH"**
- Install Python 3.7+ from python.org
- Make sure to check "Add Python to PATH" during installation
- Restart Command Prompt after installation

**"app.py not found"**
- Make sure you're running the script from the project root directory
- Check that all project files are properly downloaded/cloned

**"Port 5000 already in use"**
- Another application is using port 5000
- Kill the existing process or change the port in `app.py`

**"Import errors"**
- Install dependencies: `pip install -r requirements.txt`
- Make sure you're using the correct Python environment

## 📝 Logs and Debugging

- Server logs appear in the terminal/command window
- For detailed debugging, check the Flask debug output
- Use browser developer tools (F12) to check for JavaScript errors

## 🛑 Stopping the Server

- **Windows batch script:** Press `Ctrl+C` in the command window
- **Manual command:** Press `Ctrl+C` in the terminal
- **Docker:** `docker stop <container-id>`

## 📋 Quick Start Checklist

- [ ] Python 3.7+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Double-click `start_server.bat` (Windows) or run `python app.py`
- [ ] Open browser to http://localhost:5000
- [ ] Upload a RocketChat support dump ZIP file
- [ ] Analyze your data!

---

**Need help?** Check the main README.md or open an issue on GitHub.
