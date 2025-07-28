# 🚀 Rocket.Chat Support Dump Analyzer

This tool analyzes Rocket.Chat support dumps and logs, providing visual insights, error recommendations, and secure data handling. It is designed for administrators and support teams to quickly identify and resolve issues in Rocket.Chat deployments.

**Current Version:** v2.1.0

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![Latest Release](https://img.shields.io/github/v/release/Canepro/rocketchat-log-analyzer?label=Latest%20Release\&color=brightgreen)](https://github.com/Canepro/rocketchat-log-analyzer/releases)

---

## ![Screenshot of the Analyzer's Dashboard](https://github.com/user-attachments/assets/419f31b5-36ea-47e4-b731-cb675f578889)

## Table of Contents

* [✨ Key Features](#✨-key-features)
* [📋 Prerequisites and Installation](#📋-prerequisites-and-installation)
* [🚀 Usage](#🚀-usage)
* [🗸️ Project Roadmap](#🗸%ef%b8%8f-project-roadmap)
* [🤝 Contributing](#🤝-contributing)
* [🚐 Support](#🚐-support)
* [📄 License](#📄-license)

## ✨ Key Features

* **Visual Dashboard**: Instantly identify trends with charts for log entries over time and severity breakdowns.
* **Easy-to-use Web App**: A simple drag-and-drop interface for fast analysis.
* **Actionable Recommendations**: Get detailed solutions for common errors from an expanded knowledge base.
* **Docker Support**: Run the application in a containerized environment for maximum compatibility.
* **Secure Redaction**: Automatically redacts sensitive keywords like "password" or "token."

## 📋 Prerequisites and Installation

### Prerequisites

* **Docker** (Recommended)
* **Python 3.10+** (If not using Docker)

### Installation

1. **Clone the Repository**:

```bash
git clone https://github.com/Canepro/rocketchat-log-analyzer.git
cd rocketchat-log-analyzer
```

2. **Install Dependencies** *(if not using Docker)*:

```bash
pip install -r requirements.txt
```

## 🚀 Usage

### Using Docker (Easiest Method)

**Build the Docker Image:**

```bash
docker build -t rocketchat-analyzer .
```

**Run the Container:**

```bash
docker run -p 5000:5000 rocketchat-analyzer
```

**Open in Browser:**
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the application.

### Running Locally with Python

**Start the Server:**

```bash
python app.py
```

**Open in Browser:**
Visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## 🗸️ Project Roadmap

This roadmap outlines the planned evolution of the tool. For a detailed history of changes, refer to `CHANGELOG.md`.

### Version 3.0.0: The "Pro" Release *(Future)*

* [ ] Configuration Analyzer: Implement a module to check for common misconfigurations and provide proactive advice.

### Version 2.2.0: The "Hardening" Release *(Planned)*

* [ ] Security Hardening: Implement suggestions from code reviews (e.g., externalize SECRET\_KEY).
* [ ] Performance Optimization: Refactor the log analyzer to stream large files more efficiently.
* [ ] Code Quality: Add a basic suite of unit tests.

### Version 2.1.1: Interactive Dashboard *(Next Up)*

* [ ] Priority 1: Implement click-to-filter and hover-to-preview functionality on the timeline chart.

### Version 2.1.0: The "Dashboard & Visualization" Release (**✅ Current**)

* [x] Visual Dashboard: Added a new "Dashboard" tab with Chart.js visualizations.
* [x] Docker Support: Added a Dockerfile for easy, containerized deployment.
* [x] Intuitive Colors: Implemented a logical color scheme for the log severity chart.
* [x] Expanded Knowledge Base: Updated the knowledge base with more detailed error descriptions and solutions.
* [x] Python Version Fix: Updated type hinting for compatibility with Python 3.10+.

## 🤝 Contributing

Contributions are welcome! If you have a feature request, bug report, or a code contribution, please open a pull request.

## 🚐 Support

Please open an issue on GitHub for questions or bug reports.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
