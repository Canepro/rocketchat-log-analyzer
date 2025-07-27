# 🚀 Rocket.Chat Support Dump Analyzer

**Current Version:** v1.2.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)  
[![Latest Release](https://img.shields.io/github/v/release/Canepro/rocketchat-log-analyzer?label=Latest%20Release&color=brightgreen)](https://github.com/Canepro/rocketchat-log-analyzer/releases)

A Python tool that automates the analysis of Rocket.Chat support dumps. The tool can be run via a simple web interface or a command-line script to generate a user-friendly HTML report.

![HTML Report Screenshot](https://i.imgur.com/g0rGf13.png)

---

## ✨ Key Features

- 🔍 **Dual Interface**: Run analysis via an easy-to-use **Web App** or the traditional **Command-Line Interface**.  
- 📊 **Interactive HTML Report**: Generates a single, self-contained HTML file with interactive tables.  
- 🎯 **Actionable Recommendations**: Provides a knowledge base with detailed solutions for common errors.  
- 🔐 **Secure Redaction**: Automatically redacts sensitive keywords like `password`, `secret`, or `token`.  
- ⚡ **Robust Parsing**: Correctly handles nested JSON logs and structural variations.

---

## 🚀 Usage

This tool can be run in two ways. The web app is recommended for most users.

### Web App (Recommended)

1. **Start the Server**  
   From the project's root directory, run:
   ```bash
   python app.py
   ````

2. **Open in Browser**
   Navigate to `http://127.0.0.1:5000/` in your web browser.
3. **Upload & Analyze**
   Click the upload area to select your support dump `.zip` file, or drag-and-drop it onto the page. The analysis will run automatically and the report will be displayed in your browser.

### Command-Line Interface (CLI)

For advanced users or automation, you can still use the original `main.py` script:

```bash
# Example: Analyze a dump and save the report in the 'reports/' directory
python main.py /path/to/your/support-dump-directory --output-dir ./reports
```

---

## 📋 Prerequisites & Installation

* **Python 3.8+**
* **Packages** listed in `requirements.txt`

```bash
# Clone the repository
git clone https://github.com/Canepro/rocketchat-log-analyzer.git
cd rocketchat-log-analyzer

# Install dependencies
pip install -r requirements.txt
```

---

## 🗺️ Project Roadmap & Changelog

This roadmap outlines the planned evolution of the tool. For a detailed history of changes, see the [CHANGELOG.md](./CHANGELOG.md).

### Version 2.1.0: The "Pro" Release (Planned)

* [ ] **Priority 1: Configuration Best-Practices Analyzer**: Implement a new module to check for common misconfigurations.

### Version 2.0.0: The "Interactive Web App" Release (In Progress)

* [x] **Priority 1: Web Interface with Flask/FastAPI**: A web application for easy drag-and-drop file uploads and instant report viewing has been implemented.
* [ ] **Priority 2: Visualizations with Chart.js**: Add a dashboard with charts for a high-level overview.

### Version 1.2.0: "Smarter Analysis" Release (Latest)

* [x] **Advanced Recommendations**: Implemented an external `knowledge_base.json` with regex matching.
* [x] **Interactive Data Tables**: Integrated DataTables.js for search, sorting, and pagination.

---

## 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or code contribution, please:

1. **Fork the Repository**: Create your own copy.
2. **Create a Feature Branch**:

   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit Your Changes**:

   ```bash
   git commit -m "Add some AmazingFeature"
   ```
4. **Push to the Branch**:

   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**: Submit your changes for review.

---

## 🆘 Support

Please open an [issue on GitHub](https://github.com/Canepro/rocketchat-log-analyzer/issues) for questions or bug reports.

---

## 📄 License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the `LICENSE` file for details.

```

Let me know if you’d like this dropped directly into your `README.md` or if you want to add any badges for testing status, coverage, etc.
```
