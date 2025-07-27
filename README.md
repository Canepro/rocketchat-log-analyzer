# 🚀 Rocket.Chat Support Dump Analyzer

**Current Version:** v1.2.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Latest Release](https://img.shields.io/github/v/release/Canepro/rocketchat-log-analyzer?label=Latest%20Release&color=brightgreen)](https://github.com/Canepro/rocketchat-log-analyzer/releases)

A Python tool that automates the analysis of Rocket.Chat support dumps. The tool parses multiple JSON files from a dump, redacts sensitive information, and generates a single, user-friendly HTML report to help diagnose server issues.

[HTML Report Screenshot]
<img width="1252" height="718" alt="Screenshot_2" src="https://github.com/user-attachments/assets/6de8dbb0-ef03-4f55-bbfd-6ad45a2f2cb2" />

---

## ✨ Key Features

- 🔍 **Comprehensive Analysis**: Parses statistics, settings, apps, omnichannel configs, and logs.
- 📊 **Interactive HTML Report**: Generates a single, self-contained HTML file with interactive tables.
- 🎯 **Actionable Recommendations**: Provides a knowledge base with detailed solutions for common errors.
- 🔐 **Secure Redaction**: Automatically redacts sensitive keywords like "password," "secret," or "token."
- ⚡ **Robust Parsing**: Correctly handles nested JSON logs and structural variations.
- 🖥️ **Cross-Platform**: Runs on any system with Python 3.8+.

---

## 🚀 Quick Start

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Canepro/rocketchat-log-analyzer.git
   cd rocketchat-log-analyzer
````

2. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Analysis**
   Provide the path to your unzipped support dump directory.

   ```bash
   python main.py /path/to/your/support-dump-directory
   ```

   Your HTML report will be generated and opened in your browser automatically.

---

## 📋 Prerequisites

* A Rocket.Chat support dump (unzipped into a directory).
* Python 3.8+
* Packages from `requirements.txt`.

---

## ⚙️ Usage and Options

The tool offers several command-line arguments to customize its behavior.

| Argument        | Description                                                                  |
| --------------- | ---------------------------------------------------------------------------- |
| `dump_path`     | **(Required)** The path to the support dump directory.                       |
| `--output-dir`  | Directory to save the generated reports. *Default: `reports/`*               |
| `--log-level`   | Minimum log level to report (e.g., 30 for WARNING). *Default: 50 (CRITICAL)* |
| `--json-output` | Also output the raw analysis data as a JSON file.                            |
| `--no-browser`  | Prevents the script from automatically opening the HTML report.              |

**Example with advanced options:**

```bash
# Analyze a dump, report all logs from WARNING level up, and save a JSON copy
python main.py /path/to/dump --log-level 30 --json-output
```

---

## 🗺️ Project Roadmap & Changelog

This roadmap outlines the planned evolution of the tool. For a detailed history of changes, see the `CHANGELOG.md`.

### Version 2.1.0: The "Pro" Release *(Planned)*

* [ ] **Priority 1:** Configuration Best-Practices Analyzer — Implement a new module to check for common misconfigurations and provide proactive advice.

### Version 2.0.0: The "Interactive Web App" Release *(Planned)*

* [ ] **Priority 1:** Web Interface with Flask/FastAPI — Develop a web app for easy file uploads and report viewing.
* [ ] **Priority 2:** Visualizations with Chart.js — Add a dashboard with charts for a high-level overview.

### Version 1.2.0: "Smarter Analysis" Release *(Latest)*

* [x] **Advanced Recommendations** — Implemented an external `knowledge_base.json` with regex matching for flexible, detailed, and sourced recommendations.
* [x] **Interactive Data Tables** — Integrated DataTables.js to add search, sorting, and pagination to all tables in the HTML report.

---

## 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or a code contribution, please follow these steps:

1. **Fork the Repository** — Create your own copy of the project.
2. **Create a Feature Branch**

   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit Your Changes**

   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the Branch**

   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request** — Submit your changes for review.

---

## 🆘 Support

Please open an [issue on GitHub](https://github.com/Canepro/rocketchat-log-analyzer/issues) for questions or bug reports.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.

```

Let me know if you want this dropped into your `README.md` or if you'd like to include badges for testing status, coverage, etc.
```
