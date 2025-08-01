# 🚀 Rocket.Chat Support Dump Analyzer

**Current Version:** v2.1.4

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Latest Release](https://img.shields.io/github/v/release/Canepro/rocketchat-log-analyzer?label=Latest%20Release&color=brightgreen)](https://github.com/Canepro/rocketchat-log-analyzer/releases)
[![Docker Support](https://img.shields.io/badge/Docker-Supported-blue.svg)](https://www.docker.com/)
[![Podman Support](https://img.shields.io/badge/Podman-Compatible-purple.svg)](https://podman.io/)

---

## 📖 Overview

The **Rocket.Chat Support Dump Analyzer** is a comprehensive web-based tool designed to analyze and visualize Rocket.Chat support dump files. It provides interactive dashboards, detailed reporting, and actionable insights to help administrators diagnose issues and optimize their Rocket.Chat deployments.

### 🎯 **What Does This Tool Do?**

- **📊 Interactive Analysis**: Upload Rocket.Chat support dumps and get instant visual analysis
- **🔍 Log Analysis**: Parse and categorize log entries with severity-based filtering
- **📈 Performance Insights**: Visualize trends, errors, and system behavior over time
- **⚠️ Issue Detection**: Automatically identify common problems and provide solutions
- **📋 Comprehensive Reports**: Generate detailed HTML reports with exportable data
- **🔧 Configuration Review**: Analyze workspace settings, apps, and Omnichannel configuration

---

## ✨ Key Features

### 🎯 **Interactive Dashboard**
- **Click-to-filter charts** for log entries over time and severity breakdowns
- **Real-time filtering** with smooth transitions and visual feedback
- **Hover tooltips** with detailed information and filtering hints
- **Responsive design** that works on desktop and mobile devices

### 🎨 **Enhanced User Experience**
- **Drag-and-drop file upload** with progress indicators
- **Professional styling** with modern UI components
- **Export options** (PDF, CSV, JSON) for all data tables
- **Comprehensive notifications** for user actions and system status

### 🔧 **Reliability & Security**
- **Comprehensive error handling** with detailed error messages
- **Input validation** and secure file processing
- **ZIP bomb protection** and secure extraction
- **Automatic data redaction** for sensitive information

### 🐳 **Production Ready**
- **Docker & Podman support** with Alpine-based builds
- **Production WSGI server** (Gunicorn) for scalability
- **Environment-based configuration** for different deployment scenarios
- **CI/CD pipeline** with automated testing and security scanning

### 📚 **Intelligent Analysis**
- **Expanded knowledge base** with 100+ error patterns
- **Actionable recommendations** for common issues
- **Automated issue categorization** and priority scoring
- **Historical trend analysis** and pattern recognition

---

## �️ Prerequisites & Installation

### **System Requirements**

- **Operating System**: Windows, macOS, or Linux
- **Python**: 3.10+ (if running locally)
- **Memory**: 512MB RAM minimum (1GB+ recommended for large dumps)
- **Storage**: 100MB+ free space for temporary files
- **Browser**: Modern web browser (Chrome, Firefox, Safari, Edge)

### **Installation Options**

#### **🐳 Option 1: Docker/Podman (Recommended)**

**Advantages**: No Python setup required, isolated environment, production-ready

```bash
# Clone the repository
git clone https://github.com/Canepro/rocketchat-log-analyzer.git
cd rocketchat-log-analyzer

# Build and run with Docker
docker build -t rocketchat-analyzer .
docker run -p 5000:5000 rocketchat-analyzer

# Or with Podman
podman build -t rocketchat-analyzer .
podman run -p 5000:5000 rocketchat-analyzer
```

#### **🐍 Option 2: Local Python Installation**

**Advantages**: Direct control, easier development, no container overhead

```bash
# Clone the repository
git clone https://github.com/Canepro/rocketchat-log-analyzer.git
cd rocketchat-log-analyzer

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

#### **🪟 Option 3: Windows Quick Start**

**For Windows users seeking the easiest experience:**

1. Download/clone the repository
2. Double-click `start_server.bat`
3. Follow the on-screen instructions

The batch script includes automatic error checking and helpful guidance.

---

## 🚀 Quick Start Guide

> **📖 First time user?** Check out our comprehensive [Startup Guide](STARTUP_GUIDE.md) for detailed instructions and troubleshooting!

### **Step 1: Start the Application**

Choose your preferred method:

**🐳 Docker/Podman (Production)**
```bash
docker run -p 5000:5000 -e SECRET_KEY=your-secret-key rocketchat-analyzer
```

**🐍 Python (Development)**
```bash
python app.py
```

**🪟 Windows (Easy)**
```batch
# Double-click start_server.bat
```

### **Step 2: Access the Web Interface**

Open your browser and navigate to: **http://localhost:5000**

### **Step 3: Upload & Analyze**

1. **Upload Support Dump**: Drag and drop your Rocket.Chat support dump ZIP file
2. **Select Log Level**: Choose the minimum log level to analyze (DEBUG, INFO, WARNING, ERROR, CRITICAL)
3. **Click Analyze**: Wait for processing to complete
4. **Explore Results**: Use the interactive dashboard to investigate issues

### **Step 4: Interactive Analysis**

- **📊 Dashboard Tab**: Overview charts with click-to-filter functionality
- **📋 Summary Tab**: Key statistics and system information  
- **⚠️ Recommendations Tab**: Automated issue detection and solutions
- **📈 Statistics Tab**: Detailed metrics and performance data
- **⚙️ Settings Tab**: Workspace configuration analysis
- **💬 Omnichannel Tab**: Live chat and visitor management settings
- **📱 Apps Tab**: Installed applications and marketplace data
- **📝 All Logs Tab**: Complete log entries with advanced filtering

---

## 🔧 Advanced Configuration

### **Environment Variables**

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `SECRET_KEY` | Flask session encryption key | `dev-secret` | **Yes** (Production) |
| `FLASK_ENV` | Environment mode | `production` | No |
| `PORT` | Server port | `5000` | No |
| `MAX_CONTENT_LENGTH` | Max upload size | `100MB` | No |
| `LOG_LEVEL` | Application log level | `INFO` | No |

### **Production Deployment**

```bash
# Docker with production settings
docker run -d \
  --name rocketchat-analyzer \
  -p 5000:5000 \
  -e SECRET_KEY="$(openssl rand -hex 32)" \
  -e FLASK_ENV=production \
  -v $(pwd)/reports:/app/reports \
  --restart unless-stopped \
  rocketchat-analyzer

# Or with Podman
podman run -d \
  --name rocketchat-analyzer \
  -p 5000:5000 \
  -e SECRET_KEY="$(openssl rand -hex 32)" \
  -e FLASK_ENV=production \
  -v $(pwd)/reports:/app/reports:Z \
  --restart unless-stopped \
  rocketchat-analyzer
```

### **Reverse Proxy Setup (Nginx)**

```nginx
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://localhost:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        client_max_body_size 100M;
    }
}
```

---

## 📁 Project Structure

```
rocketchat-log-analyzer/
├── 📱 app.py                    # Main Flask web application
├── 🔍 analyzer.py              # Core log analysis and parsing logic
├── ⚙️ config.py                # Configuration management
├── 🛠️ utils.py                  # Utility functions and security helpers
├── 🖥️ main.py                   # Legacy CLI interface
├── 📦 requirements.txt          # Python dependencies
├── 🐳 Dockerfile               # Container build configuration
├── 🔧 gunicorn.conf.py         # Production WSGI server config
├── 🪟 start_server.bat         # Windows convenience startup script
├── 📊 knowledge_base.json      # Error patterns and solution database
├── 🌐 templates/               # HTML templates and web interface
│   ├── upload.html             # File upload interface
│   └── report_template.html    # Interactive analysis dashboard
├── 📈 reports/                 # Generated analysis reports (auto-created)
├── 🧪 tests/                   # Comprehensive test suite
│   ├── test_basic.py           # Core functionality tests
│   ├── test_security.py        # Security validation tests
│   └── test_support_dump.zip   # Sample test data
├── 📚 docs/                    # Documentation
│   ├── DOCKER.md               # Container deployment guide
│   ├── SECURITY.md             # Security considerations
│   └── API.md                  # API documentation
├── 🔄 .github/workflows/       # CI/CD automation
│   ├── ci.yml                  # Continuous integration
│   └── security.yml            # Security scanning
├── 📋 CHANGELOG.md             # Detailed version history
├── 🗺️ ROADMAP.md                # Development roadmap and future plans
├── 📖 STARTUP_GUIDE.md         # Comprehensive startup instructions
└── 📄 README.md                # This file
```

---

## 📊 What Can This Tool Analyze?

### **📈 Supported Data Types**

| Data Type | Description | Analysis Features |
|-----------|-------------|-------------------|
| **🗃️ Log Files** | Application, system, and error logs | Severity analysis, trend detection, error categorization |
| **⚙️ Configuration** | Workspace settings and parameters | Security audit, performance optimization |
| **� Apps & Integrations** | Installed marketplace apps | Compatibility checks, resource usage |
| **💬 Omnichannel** | Live chat and visitor data | Queue analysis, agent performance |
| **📊 Statistics** | System metrics and performance | Resource utilization, bottleneck identification |
| **⚠️ Errors & Warnings** | Issue detection and categorization | Root cause analysis, solution recommendations |

### **🎯 Analysis Capabilities**

- **📈 Trend Analysis**: Identify patterns in log frequency and error rates
- **🔍 Root Cause Detection**: Automated analysis of error chains and dependencies  
- **⚡ Performance Insights**: Server response times, resource utilization, bottlenecks
- **🔒 Security Audit**: Configuration vulnerabilities, access patterns, threats
- **📊 Visual Reporting**: Interactive charts, filtering, and data export
- **💡 Recommendations**: Actionable solutions based on identified issues

---

## 🔍 Troubleshooting

### **Common Issues & Solutions**

#### **🚫 "Cannot connect to server"**
- Verify the application is running: `docker ps` or check terminal output
- Check port availability: `netstat -an | grep 5000`
- Try a different port: `docker run -p 8080:5000 rocketchat-analyzer`

#### **📁 "Upload failed" or "File too large"**
- Maximum file size is 100MB by default
- Increase limit: `-e MAX_CONTENT_LENGTH=200000000` (200MB)
- Ensure the ZIP file is a valid Rocket.Chat support dump

#### **🐍 "Python not found" (Windows)**
- Install Python 3.10+ from [python.org](https://python.org)
- Ensure "Add Python to PATH" is checked during installation
- Restart command prompt after installation

#### **🔐 "Secret key error" (Production)**
- Generate a secure key: `openssl rand -hex 32`
- Set environment variable: `-e SECRET_KEY=your-generated-key`

#### **📊 "Charts not loading"**
- Clear browser cache and cookies
- Check browser console for JavaScript errors (F12)
- Ensure support dump contains log data

#### **🐳 "Docker build failed"**
- Update Docker to the latest version
- Clear Docker cache: `docker system prune`
- Check internet connectivity for package downloads

### **📞 Getting Help**

1. **📖 Documentation**: Check [STARTUP_GUIDE.md](STARTUP_GUIDE.md) for detailed instructions
2. **🐛 Bug Reports**: Open an [issue on GitHub](https://github.com/Canepro/rocketchat-log-analyzer/issues)
3. **💡 Feature Requests**: Use GitHub discussions or issues
4. **🔧 Technical Support**: Include log output and system information

---

## 🚀 Development & Roadmap

For comprehensive development plans and version history, see:
- **📋 [CHANGELOG.md](CHANGELOG.md)** - Detailed version history and changes
- **🗺️ [ROADMAP.md](ROADMAP.md)** - Future features and development timeline

### **🏆 Current Release: v2.1.4 "Stability & Functionality"**

**🎯 Focus**: Core functionality reliability and user experience improvements

✅ **Achievements**:
- Fixed DataTable reinitialization errors preventing chart interactions
- Enhanced chart click-to-filter functionality for timeline data
- Improved Settings tab layout with proper table formatting
- Added comprehensive startup documentation and Windows batch script
- Resolved template structure issues and duplicate code blocks

⚠️ **Known Issues**:
- Severity chart filtering redirects correctly but doesn't apply filters (low priority)

### **📈 Recent Releases**

#### **v2.1.3: "Interactive Experience"**
✅ Interactive dashboard with click-to-filter charts  
✅ Enhanced UX with tooltips, animations, and export features  
✅ Real-time filtering and comprehensive error handling  

#### **v2.1.2: "Security & Quality"**  
✅ Security hardening with externalized configurations  
✅ Comprehensive testing and CI/CD pipeline  
✅ Production-ready Docker builds with Alpine Linux  

#### **v2.1.1: "Performance & Stability"**
✅ Optimized log parsing for large files  
✅ Memory usage improvements  
✅ Enhanced error reporting and debugging  

### **🔮 Coming Soon**

- **🎨 Modern UI/UX Overhaul**: Contemporary design with improved accessibility
- **📊 Advanced Analytics**: Machine learning-based pattern detection
- **🔄 Real-time Monitoring**: Live log streaming and alerts
- **🌐 Multi-tenant Support**: Organization and team management
- **📱 Mobile Optimization**: Responsive design for tablets and phones

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### **🐛 Bug Reports**
- Use the [GitHub issue tracker](https://github.com/Canepro/rocketchat-log-analyzer/issues)
- Include detailed steps to reproduce
- Attach log files and system information
- Check existing issues to avoid duplicates

### **💡 Feature Requests**
- Open a [GitHub discussion](https://github.com/Canepro/rocketchat-log-analyzer/discussions) first
- Describe the use case and expected benefit
- Provide mockups or examples if applicable

### **🔧 Code Contributions**
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes with tests
4. Follow the existing code style
5. Submit a pull request with detailed description

### **📚 Documentation**
- Improve existing documentation
- Add examples and use cases
- Translate to other languages
- Create video tutorials or guides

### **🧪 Testing**
- Run the test suite: `python -m pytest`
- Test with different Rocket.Chat versions
- Validate with various support dump formats
- Report compatibility issues

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### **Third-Party Licenses**
- **Flask**: BSD-3-Clause License
- **Chart.js**: MIT License  
- **DataTables**: MIT License
- **Gunicorn**: MIT License

---

## 🙏 Acknowledgments

- **Rocket.Chat Team**: For creating an amazing platform and providing support dump formats
- **Open Source Community**: For the excellent libraries and tools that make this project possible
- **Contributors**: Everyone who has reported bugs, suggested features, or contributed code
- **Users**: Beta testers and early adopters who provided valuable feedback

---

## � Support & Contact

### **🆘 Getting Help**
- **📖 Documentation**: Start with [STARTUP_GUIDE.md](STARTUP_GUIDE.md)
- **🐛 Issues**: [GitHub Issues](https://github.com/Canepro/rocketchat-log-analyzer/issues)
- **💬 Discussions**: [GitHub Discussions](https://github.com/Canepro/rocketchat-log-analyzer/discussions)
- **📧 Security**: Report security issues privately via GitHub Security Advisories

### **📊 Project Stats**
- **⭐ Stars**: Help us grow by starring the repository
- **🍴 Forks**: Fork and customize for your needs
- **📦 Releases**: Stay updated with the latest versions
- **📈 Activity**: Active development with regular updates

---

<div align="center">

**Made with ❤️ for the Rocket.Chat Community**

[⭐ Star this project](https://github.com/Canepro/rocketchat-log-analyzer) | [🐛 Report Bug](https://github.com/Canepro/rocketchat-log-analyzer/issues) | [💡 Request Feature](https://github.com/Canepro/rocketchat-log-analyzer/discussions)

</div>

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.
