# main.py
import argparse
import webbrowser
import logging
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
    parser.add_argument("--no-browser", action="store_true", help="Do not open the report in a browser.")
    args = parser.parse_args()

    if not args.dump_path.is_dir():
        logging.error(f"Directory not found at '{args.dump_path}'")
        return

    # Configuration for each report section
    report_sections = {
        'summary': {'pattern': 'log.json', 'analyzer': analyzer.analyze_logs, 'headers': ['Message', 'Count', 'LastSeen'], 'title': 'Error Summary'},
        'statistics': {'pattern': 'server-statistics.json', 'analyzer': analyzer.analyze_statistics, 'headers': ['Statistic', 'Value'], 'title': 'Server Statistics'},
        'settings': {'pattern': 'settings.json', 'analyzer': analyzer.analyze_settings, 'headers': ['Setting', 'Value'], 'title': 'Workspace Settings'},
        'omnichannel': {'pattern': 'omnichannel-settings.json', 'analyzer': analyzer.analyze_omnichannel, 'headers': ['Setting', 'Value'], 'title': 'Omnichannel Settings'},
        'apps': {'pattern': 'apps-installed.json', 'analyzer': analyzer.analyze_apps, 'headers': ['Name', 'Version', 'Status'], 'title': 'Installed Apps'},
        'logs': {'pattern': 'log.json', 'analyzer': analyzer.analyze_logs, 'headers': ['level', 'time', 'pid', 'hostname', 'name', 'msg'], 'title': 'All Log Entries (Errors)'},
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
    log_data = analyzer.analyze_logs(files_found['logs']) if files_found['logs'] else {'summary': [], 'all_errors': []}

    for key, config in report_sections.items():
        content = []
        if key == 'summary':
            content = log_data['summary']
        elif key == 'logs':
            content = log_data['all_errors']
        else:
            file_path = files_found[key]
            if file_path:
                content = config['analyzer'](file_path)

        results[key] = {
            'title': config['title'],
            'content': content,
            'headers': config['headers']
        }
    
    # Generate Report
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    output_filename = f"RocketChat-Analysis-Report_{timestamp}.html"
    args.output_dir.mkdir(exist_ok=True)
    output_path = args.output_dir / output_filename
    
    generated_path = reporter.generate_report(results, output_path)
    logging.info(f"HTML report saved to: {generated_path}")
    
    if not args.no_browser:
        try:
            webbrowser.open(output_path.resolve().as_uri())
        except Exception as e:
            logging.warning(f"Could not open report automatically: {e}")

if __name__ == "__main__":
    main()