# 📄 Changelog

All notable changes to this project will be documented in this file.  
The format is based on [Keep a Changelog](https://keepachangelog.com/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [2.1.1] - In Development

### Added
- **Interactive Charts**: Implement hover-to-preview and click-to-filter functionality on the dashboard's timeline chart.

---

## [2.1.0] - 2025-07-28

### Added
- **Visual Dashboard**: Introduced a new "Dashboard" tab with Chart.js to visualize log entries over time and severity breakdown.
- **Docker Support**: Added a `Dockerfile` for easy, containerized deployment using Docker or Podman.

### Changed
- **Knowledge Base**: Significantly expanded `knowledge_base.json` with a more detailed structure, including categories, common causes, and troubleshooting steps.
- **Report Template**: Updated the report to display the new dashboard and the expanded recommendation format.
- **Python Requirement**: Updated the required Python version to **3.10+** due to the use of modern type hinting.

### Fixed
- **Python Compatibility**: Addressed a `TypeError` by updating type hints to ensure compatibility across recent Python 3 versions.
- **JSON Serialization Error**: Resolved a recurring `TypeError` by gracefully handling log entries that were missing timestamps.
- **Report Rendering**: Fixed a bug that caused several data tables in the report to appear empty.

---

## [2.0.0] - 2025-07-27

### Added
- **Flask Web Interface**: Implemented a web application (`app.py`) for a user-friendly experience.
- **Drag-and-Drop Upload**: The web UI features a styled upload area that supports drag-and-drop for `.zip` files.
- **In-Browser Reporting**: The analysis is now run on the backend, and the final HTML report is rendered directly in the browser.

### Changed
- **Dependencies**: Added `Flask` to `requirements.txt`.

---

## [1.2.0] - 2025-07-27

### Added
- **External Knowledge Base**: Created `knowledge_base.json` to manage actionable recommendations.
- **Interactive HTML Tables**: Integrated `DataTables.js` to add search, sorting, and pagination to all report tables.

---

## [1.1.0] - 2025-07-26

### Added
- **Initial Stable Release** of the Python-based analyzer.