# 🚀 Rocket.Chat Support Dump Analyzer

**Current Version:** v2.1.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Latest Release](https://img.shields.io/github/v/release/Canepro/rocketchat-log-analyzer?label=Latest%20Release\&color=brightgreen)](https://github.com/Canepro/rocketchat-log-analyzer/releases)

---

## 📊 Analyzer Dashboard Preview

![Screenshot of the Analyzer's Dashboard](https://github.com/Canepro/rocketchat-log-analyzer/blob/main/Screenshot_3.png?raw=true)

> Example view of the Rocket.Chat log analyzer dashboard in version 2.1.0


## ✨ Key Features

* **Visual Dashboard**: Instantly identify trends with charts for log entries over time and severity breakdowns.
* **Easy-to-use Web App**: A simple drag-and-drop interface for fast analysis.
* **Actionable Recommendations**: Get detailed solutions for common errors from an expanded knowledge base.
* **Docker & Podman Support**: Run the application in a containerized environment for maximum compatibility.
* **Secure Redaction**: Automatically redacts sensitive keywords like "password" or "token."

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

## 🗸️ Project Roadmap

For a comprehensive roadmap including future features and development plans, see [`ROADMAP.md`](ROADMAP.md). For detailed change history, see `CHANGELOG.md`.

### 🚧 **Currently in Development (v2.1.2)**

* **Security Hardening**: Externalizing SECRET_KEY, adding input validation, ZIP bomb protection
* **Code Quality**: Comprehensive testing, dependency management, architecture improvements
* **CI/CD Pipeline**: Automated testing and security scanning
* **Docker Improvements**: Production-ready Dockerfile with Gunicorn, security hardening, health checks

### ✅ **Version 2.1.0: The "Dashboard & Visualization" Release (Current)**

  * ✅ **Visual Dashboard**: Added a new "Dashboard" tab with Chart.js visualizations.
  * ✅ **Docker Support**: Added a `Dockerfile` for easy, containerized deployment.
  * ✅ **Intuitive Colors**: Implemented a logical color scheme for the log severity chart.
  * ✅ **Expanded Knowledge Base**: Updated the knowledge base with more detailed error descriptions and solutions.
  * ✅ **Python Version Fix**: Updated type hinting for compatibility with Python 3.10+.

---

## 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or a code contribution, please open a pull request.

---

## 🚐 Support

Please open an [issue on GitHub](https://github.com/Canepro/rocketchat-log-analyzer/issues) for questions or bug reports.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.
