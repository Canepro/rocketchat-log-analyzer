# main.py
import argparse
import webbrowser
import logging
import json
from datetime import datetime
from pathlib import Path
import analyzer
import reporter

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def find_file(directory: Path, pattern: str):
    """Finds the first file in a directory that matches a pattern."""
    try:
        return next(directory.glob(f'*{pattern}'))
    except StopIteration:
        return None

def main():
    parser = argparse.ArgumentParser(description="Analyze Rocket.Chat support dumps.")
    parser.add_argument("dump_path", type=Path, help="Path to the support dump directory.")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).parent / 'reports', help="Directory for output reports.")
    parser.add_argument("--log-level", type=int, default=50, help="Minimum log level to report (e.g., 30 for WARNING, 40 for ERROR).")
    parser.add_argument("--json-output", action="store_true", help="Output a JSON file with the raw analysis results.")
    parser.add_argument("--no-browser", action="store_true", help="Do not open the report in a browser.")
    args = parser.parse_args()

    if not args.dump_path.is_dir():
        logging.error(f"Directory not found at '{args.dump_path}'")
        return

    # Configuration for each report section
    report_sections = {
        'recommendations': {'pattern': 'log.json', 'title': 'Recommendations'},
        'summary': {'pattern': 'log.json', 'headers': ['Message', 'Count', 'LastSeen'], 'title': 'Error Summary'},
        'statistics': {'pattern': 'server-statistics.json', 'analyzer': analyzer.analyze_statistics, 'headers': ['Statistic', 'Value'], 'title': 'Server Statistics'},
        'settings': {'pattern': 'settings.json', 'analyzer': analyzer.analyze_settings, 'headers': ['Setting', 'Value'], 'title': 'Workspace Settings'},
        'omnichannel': {'pattern': 'omnichannel-settings.json', 'analyzer': analyzer.analyze_omnichannel, 'headers': ['Setting', 'Value'], 'title': 'Omnichannel Settings'},
        'apps': {'pattern': 'apps-installed.json', 'analyzer': analyzer.analyze_apps, 'headers': ['Name', 'Version', 'Status'], 'title': 'Installed Apps'},
        'logs': {'pattern': 'log.json', 'headers': ['level', 'time', 'pid', 'hostname', 'name', 'msg'], 'title': 'All Log Entries'},
    }

    logging.info("--- Finding files in dump directory ---")
    files_found = {}
    for key, config in report_sections.items():
        if key == 'settings':
            all_settings = list(args.dump_path.glob('*settings.json'))
            file_path = next((f for f in all_settings if 'omnichannel' not in f.name.lower()), None)
        else:
            file_path = find_file(args.dump_path, config['pattern'])
        files_found[key] = file_path
        logging.info(f"{config['title']:<25} File: {file_path.name if file_path else 'Not Found'}")
    logging.info("---------------------------------------")

    # Analyze data and build results
    results = {}
    log_data = analyzer.analyze_logs(files_found['logs'], args.log_level) if files_found['logs'] else \
               {'summary': [], 'all_errors': [], 'total_error_count': 0, 'recommendations': []}

    statistics_content = analyzer.analyze_statistics(files_found['statistics']) if files_found['statistics'] else []
    version = next((item['Value'] for item in statistics_content if item['Statistic'] == 'Version'), 'N/A')
    logging.info(f"Detected Rocket.Chat Version: {version}")

    for key, config in report_sections.items():
        # Handle log-derived sections first
        if key == 'recommendations':
            results[key] = {'title': config['title'], 'content': log_data['recommendations']}
            continue
        if key == 'summary':
            results[key] = {'title': config['title'], 'content': log_data['summary'], 'headers': config['headers']}
            continue
        if key == 'logs':
            results[key] = {'title': config['title'], 'content': log_data['all_errors'], 'headers': config['headers'], 'total_count': log_data['total_error_count']}
            continue

        # Handle other file-based sections
        if key == 'statistics':
             results[key] = {'title': config['title'], 'content': statistics_content, 'headers': config['headers']}
             continue

        file_path = files_found[key]
        content = config['analyzer'](file_path) if file_path else []
        results[key] = {'title': config['title'], 'content': content, 'headers': config['headers']}

    # Generate Report
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    args.output_dir.mkdir(exist_ok=True)
    
    # HTML Report
    output_filename_html = f"RocketChat-Analysis-Report_{timestamp}.html"
    output_path_html = args.output_dir / output_filename_html
    generated_path = reporter.generate_report(results, output_path_html)
    logging.info(f"HTML report saved to: {generated_path}")

    # Optional JSON Output
    if args.json_output:
        output_filename_json = f"RocketChat-Analysis-Report_{timestamp}.json"
        output_path_json = args.output_dir / output_filename_json
        with open(output_path_json, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)
        logging.info(f"JSON output saved to: {output_path_json}")

    if not args.no_browser:
        try:
            webbrowser.open(output_path_html.resolve().as_uri())
        except Exception as e:
            logging.warning(f"Could not open report automatically: {e}")

if __name__ == "__main__":
    main()