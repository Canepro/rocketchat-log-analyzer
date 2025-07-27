# 🚀 Rocket.Chat Support Dump Analyzer

**Current Version:** v1.1.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Status](https://img.shields.io/badge/Status-In%20Development-blue.svg)]()

A Python tool that automates the analysis of Rocket.Chat support dumps. The tool parses multiple JSON files from a dump, redacts sensitive information, and generates a single, user-friendly HTML report to help diagnose server issues.

![HTML Report Screenshot](https://i.imgur.com/g0rGf13.png)

## ✨ Key Features

-   🔍 **Comprehensive Analysis**: Parses statistics, settings, apps, omnichannel configs, and logs.
-   📊 **Interactive HTML Report**: Generates a single, self-contained HTML file with interactive tables.
-   🎯 **Actionable Recommendations**: Provides a knowledge base with detailed solutions for common errors.
-   🔐 **Secure Redaction**: Automatically redacts sensitive keywords like "password," "secret," or "token."
-   ⚡ **Robust Parsing**: Correctly handles nested JSON logs and structural variations.
-   🖥️ **Cross-Platform**: Runs on any system with Python 3.8+.

---
## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Canepro/rocketchat-log-analyzer.git
    ````

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Analysis**

   ```bash
   python main.py /path/to/your/support-dump-directory
   ```

   The HTML report will be generated and opened automatically in your browser.

---

## 📋 Prerequisites

* A Rocket.Chat support dump (unzipped).
* Python 3.8 or later.
* Packages from `requirements.txt`.

---

## ⚙️ Usage and Options

| Argument        | Description                                                       |
| --------------- | ----------------------------------------------------------------- |
| `dump_path`     | **(Required)** Path to the support dump directory.                |
| `--output-dir`  | Directory to save reports. *Default: `reports/`*                  |
| `--log-level`   | Minimum log level (e.g. 30 for WARNING). *Default: 50 (CRITICAL)* |
| `--json-output` | Also output raw analysis data as a JSON file.                     |
| `--no-browser`  | Prevents automatic opening of the HTML report.                    |

**Example:**

```bash
python main.py /path/to/dump --log-level 30 --json-output
```

---

## 🗺️ Project Roadmap & Changelog

This roadmap outlines the planned evolution of the tool. For a detailed history of changes, see the [CHANGELOG.md](CHANGELOG.md).

### **Version 1.2.0: The "Smarter Analysis" Release (In Progress)**

-   [x] **Priority 1: Advanced Recommendations**: Implemented an external `knowledge_base.json` with regex matching for flexible, detailed, and sourced recommendations.
-   [x] **Priority 2: Interactive Data Tables**: Integrated DataTables.js to add search, sorting, and pagination to all tables in the HTML report.

### **Version 2.0.0: The "Interactive Web App" Release (Planned)**

-   [ ] **Priority 1: Web Interface with Flask/FastAPI**: Develop a web app for easy file uploads and report viewing.
-   [ ] **Priority 2: Visualizations with Chart.js**: Add a dashboard with charts for a high-level overview.

### **Version 2.1.0: The "Pro" Release (Planned)**

-   [ ] **Priority 1: Configuration Best-Practices Analyzer**: Implement a new module to check for common misconfigurations and provide proactive advice.

## 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or a code contribution, please follow these steps:

1.  **Fork the Repository**: Create your own copy of the project.
2.  **Create a Feature Branch**: (`git checkout -b feature/AmazingFeature`).
3.  **Commit Your Changes**: (`git commit -m 'Add some AmazingFeature'`).
4.  **Push to the Branch**: (`git push origin feature/AmazingFeature`).
5.  **Open a Pull Request**: Submit your changes for review.

## 🆘 Support

Please open an issue on GitHub for questions or bug reports.

-   🔗 [**GitHub Issues**](https://github.com/Canepro/rocketchat-log-analyzer/issues)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.