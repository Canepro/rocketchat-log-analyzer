# 🚀 Rocket.Chat Support Dump Analyzer

**Current Version:** v1.1.0  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)  
[![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)]()

A Python tool that automates the analysis of Rocket.Chat support dumps. It parses multiple JSON files, redacts sensitive data, and generates a clean HTML report to aid troubleshooting.

[HTML Report Screenshot]
<img width="3772" height="1034" alt="Screenshot_1" src="https://github.com/user-attachments/assets/63e64bfc-8341-4743-8a26-72d4e823b0dc" />

---

## ✨ Key Features

- 🔍 **Comprehensive Analysis**: Parses statistics, settings, apps, omnichannel configs, and logs.
- 📊 **Interactive HTML Report**: Generates a single, self-contained HTML file with a tabbed UI.
- 🎯 **Actionable Recommendations**: Built-in knowledge base for common issues.
- 🔐 **Secure Redaction**: Auto-redacts keywords like "password", "secret", "token", etc.
- ⚡ **Robust Parsing**: Handles nested JSON, log formats, and Rocket.Chat version differences.
- 🖥️ **Cross-Platform**: Works anywhere Python 3.8+ runs.

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

## 🗺️ Project Roadmap

### 🔧 Version 1.2.0: *The "Smarter Analysis" Release*

* **Advanced Recommendations**
  Externalize `knowledge_base.json` for richer, linked solutions.

* **Interactive Data Tables**
  Add `DataTables.js` to allow search, sorting, and pagination in reports.

---

### 🌐 Version 2.0.0: *The "Interactive Web App" Release*

* **Web Interface (Flask/FastAPI)**
  Users upload `.zip` files through a webpage and view reports instantly.

* **Visualizations with Chart.js**
  Add a "Dashboard" tab with error timelines and log severity pie charts.

---

### 💼 Version 2.1.0: *The "Pro" Release*

* **Configuration Best-Practices Analyzer**
  Add a "Configuration Health" section based on environment checks (e.g. warn if GridFS is used in production).

---

## 🤝 Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature/your-amazing-feature
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add amazing feature"
   ```
4. Push to your fork:

   ```bash
   git push origin feature/your-amazing-feature
   ```
5. Open a Pull Request.

---

## 🆘 Support

Please open an issue on GitHub for questions or bug reports.
🔗 [GitHub Issues](https://github.com/Canepro/rocketchat-log-analyzer/issues)

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```

Let me know if you want a separate `README.md` file output or a version with badges or code snippets customized.
```
