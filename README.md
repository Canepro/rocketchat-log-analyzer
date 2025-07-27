# 🚀 Rocket.Chat Support Dump Analyzer

**Current Version:** v2.0.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Latest Release](https://img.shields.io/github/v/release/Canepro/rocketchat-log-analyzer?label=Latest%20Release\&color=brightgreen)](https://github.com/Canepro/rocketchat-log-analyzer/releases)

---

[Screenshot of the Web App UI]
<img width="2331" height="1267" alt="Screenshot_3" src="https://github.com/user-attachments/assets/419f31b5-36ea-47e4-b731-cb675f578889" />

---

## ✨ Key Features

* 🔍 **Easy-to-use Web App**: The primary interface is a web application for simple drag-and-drop analysis.
* ⚙️ **Interactive Log-Level Filtering**: Dynamically filter the analysis by log severity (e.g., ERROR, WARNING) directly in the UI.
* 📊 **Interactive HTML Report**: Generates a single, self-contained HTML file with searchable and sortable tables.
* 🎯 **Actionable Recommendations**: Uses a knowledge base to identify common errors and provide detailed solutions.
* 🔐 **Secure Redaction**: Automatically redacts sensitive keywords like "password," "secret," or "token."
* ⚡ **Robust Parsing**: Correctly handles nested JSON logs and structural variations in support dumps.

---

## 🚀 Usage

### Web App (Recommended)

This is the easiest way to analyze a support dump.

#### 1. Start the Server

From the project's root directory, run the following command in your terminal:

```bash
python app.py
```

#### 2. Open in Browser

Navigate to `http://127.0.0.1:5000/` in your web browser.

#### 3. Upload & Analyze

* Drag and drop your support dump `.zip` file onto the page, or click to select it.
* Choose the minimum log level you want to analyze.
* Click **Analyze**.
* The report will be generated and displayed directly in your browser.

### Command-Line Interface (CLI)

For advanced users or automation, the original CLI is still available.

```bash
# Example: Analyze a dump for WARNING level logs and higher
python main.py /path/to/your/support-dump-directory --log-level 30
```

---

## 📋 Prerequisites & Installation

* Python 3.8+
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

## 📜 Project Roadmap & Changelog

This roadmap outlines the planned evolution of the tool. For a detailed history of changes, see `CHANGELOG.md`.

### Version 3.0.0: The "Pro" Release (Future)

* [ ] Configuration Best-Practices Analyzer: Implement a new module to check for common misconfigurations and provide proactive advice.

### Version 2.2.0: The "Hardening" Release (Planned)

* [ ] Security Hardening: Implement suggestions from code reviews (e.g., externalize `SECRET_KEY`).
* [ ] Performance Optimization: Refactor the log analyzer to stream large files more efficiently.
* [ ] Code Quality: Add a basic suite of unit tests for core analysis functions.

### Version 2.1.0: The "Dashboard & Visualization" Release (Next Up)

* [ ] **Priority 1:** Visualizations with Chart.js: Add a new "Dashboard" tab to the report with charts for errors over time and log severity breakdown.

### Version 2.0.0: "Web App Foundation" Release (✅ Latest)

* ✅ **Web Interface**: Implemented a fully functional Flask web application (`app.py`).
* ✅ **Interactive Uploads**: Created a user-friendly interface for uploading `.zip` dumps with an interactive log level selector.
* ✅ **In-Browser Reporting**: The web app now runs the complete analysis and renders the report directly in the browser.

---

## 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or a code contribution, please follow these steps:

1. **Fork the Repository**: Create your own copy of the project.
2. **Create a Feature Branch**: (`git checkout -b feature/AmazingFeature`).
3. **Commit Your Changes**: (`git commit -m 'Add some AmazingFeature'`).
4. **Push to the Branch**: (`git push origin feature/AmazingFeature`).
5. **Open a Pull Request**: Submit your changes for review.

---

## 🚐 Support

Please open an [issue on GitHub](https://github.com/Canepro/rocketchat-log-analyzer/issues) for questions or bug reports.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.
