# 🚀 Rocket.Chat Support Dump Analyzer

**Current Version:** v2.1.4

[![License: MIT](https://img---

## 📁 Project Structure

```textlds.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Latest Release](https://img.shields.io/github/v/release/Canepro/rocketchat-log-analyzer?label=Latest%20Release\&color=brightgreen)](https://github.com/Canepro/rocketchat-log-analyzer/releases)

---

## ✨ Key Features

* **🎯 Interactive Dashboard**: Click-to-filter charts for log entries over time and severity breakdowns with real-time filtering
* **🎨 Enhanced User Experience**: Hover tooltips, smooth animations, and comprehensive export options (PDF/CSV/JSON)
* **🔧 Reliable & Secure**: Comprehensive error handling, input validation, and secure file processing
* **🌐 Easy-to-use Web App**: Modern drag-and-drop interface with professional styling
* **📚 Actionable Recommendations**: Get detailed solutions for common errors from an expanded knowledge base
* **🐳 Container Ready**: Full Docker & Podman support with Alpine-based production builds
* **🔒 Security Focused**: Automatic redaction of sensitive data, ZIP bomb protection, and secure extraction

---

## 📋 Prerequisites & Installation

### **Prerequisites**

* **Docker or Podman** (Recommended)
* **Python 3.10+** (If not using a container)

### **Installation**

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Canepro/rocketchat-log-analyzer.git
   cd rocketchat-log-analyzer
   ```

2. **Install Dependencies** *(if not using a container)*:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### **Using Docker or Podman (Recommended)**

**Note**: The Docker container now uses Python 3.12 Alpine for better security and performance, with production-grade Gunicorn WSGI server. Fully compatible with both Docker and Podman. See [`DOCKER.md`](DOCKER.md) for detailed configuration options.

1. **Build the Container Image**:
   *For Docker:*

   ```bash
   docker build -t rocketchat-analyzer .
   ```

   *For Podman:*

   ```bash
   podman build -t rocketchat-analyzer .
   ```

2. **Run the Container**:
   *For Docker (Development):*

   ```bash
   docker run -p 5000:5000 -e FLASK_ENV=development rocketchat-analyzer
   ```

   *For Docker (Production):*

   ```bash
   docker run -p 5000:5000 \
     -e SECRET_KEY=your-secure-secret-key \
     -e FLASK_ENV=production \
     rocketchat-analyzer
   ```

   *For Podman (works with same commands):*

   ```bash
   podman run -p 5000:5000 -e SECRET_KEY=your-secure-secret-key rocketchat-analyzer
   ```

3. **Open in Browser**:
   Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser to access the application.

### **Running Locally with Python**

1. **Start the Server**:

   ```bash
   python app.py
   ```

2. **Open in Browser**:
   Navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

---

## � Project Structure

```
rocketchat-log-analyzer/
├── app.py                    # Main Flask application
├── analyzer.py              # Core log analysis logic
├── config.py                # Configuration management
├── utils.py                  # Utility functions and security helpers
├── main.py                   # CLI interface (legacy)
├── requirements.txt          # Python dependencies
├── Dockerfile               # Container build configuration
├── gunicorn.conf.py         # Production WSGI server config
├── templates/               # HTML templates
│   ├── upload.html         # File upload interface
│   └── report_template.html # Interactive analysis dashboard
├── reports/                 # Generated analysis reports
├── tests/                   # Test suite
│   ├── test_basic.py       # Core functionality tests
│   └── test_support_dump.zip # Test data
├── docs/                    # Documentation
│   ├── DOCKER.md           # Container deployment guide
│   └── ROADMAP_OLD.md      # Historical roadmap
├── .github/workflows/       # CI/CD pipeline
├── knowledge_base.json      # Error patterns and solutions
├── CHANGELOG.md            # Version history
├── ROADMAP.md              # Development roadmap
└── README.md               # This file
```

---

## �🗸️ Project Roadmap

For a comprehensive roadmap including future features and development plans, see [`ROADMAP.md`](ROADMAP.md). For detailed change history, see `CHANGELOG.md`.

### ✅ **Version 2.1.4: The "Chart Filtering Fix" Release (Current)**

* ✅ **Bug Fixes**: Fixed broken chart click-to-filter functionality that was showing "0 found" results
* ✅ **DataTable Integration**: Resolved reference mismatches and improved search compatibility
* ✅ **Reliability**: Enhanced timeout handling and race condition prevention
* ✅ **User Experience**: Seamless chart-to-table filtering now works correctly

### ✅ **Version 2.1.3: The "Interactive Experience" Release**

* ✅ **Interactive Dashboard**: Click-to-filter charts with real-time log filtering
* ✅ **Enhanced UX**: Hover tooltips, smooth animations, export features (PDF/CSV/JSON)
* ✅ **Reliability**: Comprehensive error handling and user feedback systems
* ✅ **Bug Fixes**: Resolved chart stretching and filtering issues

### ✅ **Version 2.1.2: The "Security & Quality" Release**

* ✅ **Security Hardening**: Externalized SECRET_KEY, ZIP bomb protection, input validation
* ✅ **Code Quality**: Comprehensive testing, dependency management, architecture improvements
* ✅ **CI/CD Pipeline**: Automated testing and security scanning
* ✅ **Docker Improvements**: Production-ready Alpine builds with Gunicorn

---

## 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or a code contribution, please open a pull request.

---

## 🚐 Support

Please open an [issue on GitHub](https://github.com/Canepro/rocketchat-log-analyzer/issues) for questions or bug reports.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.
