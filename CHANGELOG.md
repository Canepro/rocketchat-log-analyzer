# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.2.0] - In Development

### Added
- **External Knowledge Base**: Created `knowledge_base.json` to manage actionable recommendations. It currently contains 20 detailed entries with titles, descriptions, solutions, and source links.
- **Interactive HTML Tables**: Integrated the DataTables.js library to add client-side search, sorting, and pagination to all tables in the generated HTML report, significantly improving usability.
- **Regex-Based Log Matching**: The log analyzer now uses regular expressions for more flexible and powerful matching against the knowledge base.

### Changed
- **Enhanced Recommendations**: The "Recommendations" tab in the report is now richer, displaying detailed information for each suggestion.
- **Updated Dependencies**: Added jQuery as a requirement for DataTables functionality (via CDN).

## [1.1.0] - 2024-XX-XX

### Added
- Initial stable release of the Python-based analyzer.
- Core features including parsing of settings, logs, apps, and statistics.
- Secure redaction of sensitive keywords.
- Generation of a tabbed HTML report.
