# 📄 Changelog

All notable changes to this project will be documented in this file.  
The format is based on [Keep a Changelog](https://keepachangelog.com/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [2.0.0] - In Development

### Added
- **Flask Web Interface**: Implemented a web application (`app.py`) for a user-friendly experience.
- **Drag-and-Drop Upload**: The web UI features a styled upload area that supports drag-and-drop for `.zip` files and provides immediate user feedback.
- **In-Browser Reporting**: The analysis is now run on the backend, and the final HTML report is rendered directly in the browser, removing the need to handle local files.
- **Security Enhancements**: Added `secure_filename` to sanitize uploads and a `MAX_CONTENT_LENGTH` to limit file size.

### Changed
- **`reporter.py`**: The `generate_report` function was refactored to return HTML content as a string instead of writing to a file, enabling in-browser rendering.
- **Dependencies**: Added `Flask` to `requirements.txt`.

---

## [1.2.0] - 2025-07-27

### Added
- **External Knowledge Base**: Created `knowledge_base.json` to manage actionable recommendations with 20+ detailed entries.
- **Interactive HTML Tables**: Integrated `DataTables.js` to add search, sorting, and pagination to all report tables.
- **Regex-Based Log Matching**: The analyzer now uses regular expressions for more flexible matching against the knowledge base.

### Changed
- **Enhanced Recommendations**: The "Recommendations" tab in the report is now richer, displaying detailed information.

---

## [1.1.0] - 2025-07-26

### Added
- **Initial Stable Release** of the Python-based analyzer.
- Core features including parsing of settings, logs, apps, and statistics.
- Secure redaction of sensitive keywords.
- Generation of a tabbed HTML report.
