# 🚀 Rocket.Chat Support Dump Analyzer

**Current Version:** v2.0.0 (Web App Foundation)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Latest Release](https://img.shields.io/github/v/release/Canepro/rocketchat-log-analyzer?label=Latest%20Release\&color=brightgreen)](https://github.com/Canepro/rocketchat-log-analyzer/releases)

---

![Screenshot](./assets/screenshot.png)

---

## ✨ Key Features

* 🔍 **Dual Interface**: Run analysis via an easy-to-use Web App or the traditional Command-Line Interface.
* 📊 **Interactive HTML Report**: Generates a single, self-contained HTML file with interactive tables.
* 🎯 **Actionable Recommendations**: Provides a knowledge base with detailed solutions for common errors.
* 🔐 **Secure Redaction**: Automatically redacts sensitive keywords like "password," "secret," or "token."
* ⚡ **Robust Parsing**: Correctly handles nested JSON logs and structural variations.

---

## 🚀 Usage

This tool can be run in two ways. The web app is recommended for most users.

### Web App (Recommended)

#### Start the Server

From the project's root directory, run the following command in your terminal:

```bash
python app.py
```

#### Open in Browser

Navigate to `http://127.0.0.1:5000/` in your web browser.

#### Upload & Analyze

Click the upload area to select your support dump `.zip` file, or simply drag and drop it onto the page. The analysis will run automatically, and the report will be displayed in your browser.

### Command-Line Interface (CLI)

For advanced users or automation, you can still use the original `main.py` script.

```bash
# Example: Analyze a dump and save the report in the 'reports/' directory
python main.py /path/to/your/support-dump-directory --output-dir ./reports
```

---

## 📋 Prerequisites & Installation

* **Python 3.8+**
* Packages listed in `requirements.txt`

### Clone the Repository

```bash
git clone https://github.com/Canepro/rocketchat-log-analyzer.git
cd rocketchat-log-analyzer
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🗘️ Project Roadmap & Changelog

This roadmap outlines the planned evolution of the tool. For a detailed history of changes, see the `CHANGELOG.md`.

### Version 3.0.0: The "Pro" Release (Future)

* [ ] Configuration Best-Practices Analyzer: Implement a new module to check for common misconfigurations and provide proactive advice.

### Version 2.2.0: The "Hardening" Release (Planned)

* [ ] Security Hardening: Implement suggestions from code reviews (e.g., externalize `SECRET_KEY`).
* [ ] Improved Error Handling: Make the analyzer raise specific errors for corrupted files.
* [ ] Performance Optimization: Refactor the log analyzer to stream large files.
* [ ] Code Quality: Add a basic suite of unit tests.

### Version 2.1.0: The "Dashboard & Visualization" Release (Next Up)

* [ ] **Priority 1**: Visualizations with Chart.js: Add a new "Dashboard" tab to the report with charts for errors over time and log severity breakdown.

### Version 2.0.0: "Web App Foundation" Release (Latest)

* ✅ Web Interface: Implemented a fully functional Flask web application.
* ✅ Drag-and-Drop Upload: Created a user-friendly interface for uploading `.zip` support dumps.
* ✅ Integrated Analysis Engine: The web app now runs the complete analysis and renders the report directly in the browser.

---

## 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or a code contribution, please follow these steps:

1. **Fork the Repository**: Create your own copy of the project.
2. **Create a Feature Branch**: (`git checkout -b feature/AmazingFeature`).
3. **Commit Your Changes**: (`git commit -m 'Add some AmazingFeature'`).
4. **Push to the Branch**: (`git push origin feature/AmazingFeature`).
5. **Open a Pull Request**: Submit your changes for review.

---

## 🛐 Support

Please open an [issue on GitHub](https://github.com/Canepro/rocketchat-log-analyzer/issues) for questions or bug reports.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.
