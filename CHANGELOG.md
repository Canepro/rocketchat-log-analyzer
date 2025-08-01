# 📄 Changelog

All notable changes to this project will be documented in this file.  
The format is based on [Keep a Changelog](https://keepachangelog.com/),  
and this project adheres to [Semantic Versioning](https://semver.org/).

---

## [2.1.3] - 2025-08-01 (User Experience Enhancement)

### 🎯 Interactive Dashboard Features
- **Click-to-Filter Charts**: Timeline and severity charts now support click-to-filter functionality
- **Enhanced Hover Tooltips**: Improved hover-to-preview with filtering hints and data insights
- **Smart Tab Switching**: Automatic navigation to logs tab when filtering
- **Visual Feedback**: Enhanced cursor changes, hover effects, and notification system
- **Export Features**: Added PDF, CSV, and JSON export buttons to dashboard

### 🔧 Reliability Improvements
- **Error Handling**: Comprehensive try-catch blocks for all interactive features
- **DataTable Integration**: Robust timing and initialization for table filtering
- **Console Logging**: Added debugging support for chart interactions
- **Fallback Mechanisms**: Multiple fallback options for tab switching and element detection
- **Notification System**: Multi-type notification system (info, success, error, warning)

### 🎨 User Experience
- **Better Visual Design**: Larger interactive areas, improved hover states
- **Clear Feedback**: Real-time filtering results and status messages
- **Smooth Transitions**: Animated scrolling and tab switching
- **Accessibility**: Improved keyboard and screen reader support

### 🐛 Bug Fixes
- **Chart Stretching Issue**: Fixed infinite chart stretching problem that occurred after uploading support dumps
  - Set fixed aspect ratios for both timeline and severity charts
  - Added proper resize handling with debouncing
  - Added CSS constraints to prevent chart container overflow
  - Enhanced tab switching with proper chart resize management
- **Chart Click Filtering**: Fixed chart click-to-filter functionality not properly filtering logs
  - Corrected table ID mismatch (`logsTable` vs `logs_table`)
  - Enhanced date filtering with regex search for better timestamp matching
  - Added severity level mapping for both text and numeric log levels
  - Improved error handling and fallback mechanisms

---

## [2.1.2] - 2025-08-01 (Security & Quality Release)

### 🔒 Security
- **Externalized SECRET_KEY**: Removed hardcoded secret key, now uses environment variables or secure random generation
- **ZIP File Validation**: Added comprehensive validation including size limits and zip bomb protection
- **Input Sanitization**: Enhanced filename sanitization and path traversal protection
- **Safe Extraction**: Implemented secure ZIP extraction with size limits per file

### 🏗️ Architecture & Code Quality
- **Configuration Management**: Extracted all configuration to `config.py` with environment-based configs
- **Code Deduplication**: Created `utils.py` module to eliminate code duplication
- **Type Safety**: Enhanced type hints throughout the codebase
- **Error Handling**: Improved error handling with custom exception classes

### 📦 Dependencies & Build

- **Pinned Dependencies**: Added version constraints to `requirements.txt` for security and stability
- **Environment Configuration**: Added `.env.example` for easy environment setup
- **CI/CD Pipeline**: Added GitHub Actions workflow with testing, security scanning, and Docker builds
- **Production WSGI**: Added Gunicorn for production-grade web server deployment

### 🐳 Docker & Containerization

- **Alpine Base Image**: Migrated from `python:3.11-slim` to `python:3.12-alpine` for smaller size and better security
- **Docker/Podman Compatibility**: Fully tested and compatible with both Docker and Podman container engines
- **Security Hardening**: Non-root user, system updates, minimal attack surface
- **Production Ready**: Gunicorn WSGI server instead of Flask development server
- **Health Checks**: Built-in Docker health monitoring and startup detection (Docker format)
- **Resource Management**: Configurable limits and proper temporary directory handling
- **Environment Configuration**: Comprehensive environment variable support
- **.dockerignore**: Optimized Docker build context for faster builds

### 🧪 Testing & Quality Assurance
- **Unit Tests**: Added basic test suite with pytest
- **Security Scanning**: Integrated bandit for security analysis and safety for dependency vulnerabilities
- **Code Formatting**: Added black for consistent code formatting
- **Linting**: Added flake8 for code quality checks

### 📚 Documentation
- **Project Roadmap**: Created comprehensive `ROADMAP.md` with future development plans
- **Updated README**: Enhanced README with current development status and roadmap reference

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