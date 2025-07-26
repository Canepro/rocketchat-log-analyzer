# Rocket.Chat Support Dump Analyzer

A Python tool to parse and analyze Rocket.Chat support dumps, generating a clean, interactive HTML report to help diagnose server issues quickly.

![HTML Report Screenshot]
<img width="3772" height="1034" alt="Screenshot_1" src="https://github.com/user-attachments/assets/d16f5042-739e-41a4-93de-3ce4ed311fb7" />


This tool processes key JSON files from a support dump, including server statistics, workspace settings, omnichannel configurations, installed apps, and system logs, presenting them in an easy-to-navigate tabbed interface.

## Features

-   **Comprehensive Analysis**: Parses statistics, settings, apps, omnichannel configs, and logs.
-   **Interactive HTML Report**: Generates a single, self-contained HTML file with a clean, tabbed UI.
-   **Robust Parsing**: Correctly handles different JSON structures that can vary between Rocket.Chat versions, including nested log dumps.
-   **Secure**: Automatically redacts sensitive information like passwords, secrets, and tokens from the report.
-   **Professional UI**: Prevents raw HTML in settings from breaking the report layout and includes scrollable cells for long content.
-   **Recommendations**: Provides actionable advice based on detected log issues via a knowledge base.

## Requirements

-   Python 3.8+
-   Required packages are listed in `requirements.txt`.

## Installation

1.  Clone this repository:
    ```bash
    git clone [https://github.com/Canepro/rocketchat-log-analyzer.git](https://github.com/Canepro/rocketchat-log-analyzer.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd rocketchat-log-analyzer
    ```
3.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script from your terminal, providing the path to the directory containing the unzipped support dump files.

```bash
python main.py /path/to/your/support-dump-directory

Command-Line Arguments
dump_path (Required): The path to the support dump directory.

--output-dir (Optional): Directory to save the generated reports. Defaults to a reports/ folder in the project directory.

--log-level (Optional): Minimum log level to report (e.g., 10 for DEBUG, 30 for WARNING). Defaults to 50 (CRITICAL).

--json-output (Optional): Also output raw analysis as JSON.

--no-browser (Optional): Prevents the script from automatically opening the HTML report in your web browser.

Example
# Analyze a dump and show all logs from DEBUG level up
python main.py "
