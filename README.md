# Rocket.Chat Support Dump Analyzer (v1.0.0)

A Python tool to parse and analyze Rocket.Chat support dumps, generating a clean, interactive HTML report to help diagnose server issues quickly.

This tool processes key JSON files from a support dump, including server statistics, workspace settings, omnichannel configurations, installed apps, and system logs, presenting them in an easy-to-navigate tabbed interface.

## Features

- **Comprehensive Analysis**: Parses statistics, settings, apps, omnichannel configs, and logs.
- **Interactive HTML Report**: Generates a single, self-contained HTML file with a clean, tabbed UI.
- **Robust Parsing**: Correctly handles different JSON structures that can vary between Rocket.Chat versions.
- **Secure**: Automatically redacts sensitive information like passwords, secrets, and tokens from the report.
- **Professional UI**: Prevents raw HTML in settings from breaking the report layout and includes scrollable cells for long content.

## Requirements

- Python 3.8+
- Required packages are listed in `requirements.txt`.

## Installation

1.  Clone this repository or download the source code.
2.  Navigate to the project directory:
    ```bash
    cd rocketchat-analyzer
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

--no-browser (Optional): Prevents the script from automatically opening the HTML report in your web browser.

Example
# Analyze a dump and open the report in the browser
python main.py "C:\Downloads\7.8.0-support-dump"

# Analyze a dump and save to a custom directory without opening it
python main.py "/mnt/data/rc
