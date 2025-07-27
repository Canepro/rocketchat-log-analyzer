# app.py
from flask import Flask, render_template, request, flash
import os
import tempfile
import zipfile
from pathlib import Path
from werkzeug.utils import secure_filename

# Import the analysis and reporting functions
import analyzer
import reporter

# Initialize the Flask application
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'a-super-secret-key-that-you-should-change'
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB upload limit

def find_dump_path(base_path: Path) -> Path | None:
    """Robustly finds the correct directory containing the support dump files."""
    for path in base_path.rglob('*server-statistics.json'):
        return path.parent
    if any(base_path.glob('*log.json')):
        return base_path
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'support_dump' not in request.files:
            flash('No file part in the request.', 'error')
            return render_template('upload.html')
        
        file = request.files['support_dump']

        if file.filename == '':
            flash('No selected file.', 'error')
            return render_template('upload.html')

        if file and file.filename.endswith('.zip'):
            safe_filename = secure_filename(file.filename)
            
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_path = Path(temp_dir)
                file_path = temp_path / safe_filename
                file.save(file_path)

                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_path)

                dump_path = find_dump_path(temp_path)
                
                if not dump_path:
                    flash("Upload failed: Could not find a valid Rocket.Chat dump structure.", "error")
                    return render_template('upload.html')

                report_sections = {
                    'summary': {'pattern': 'log.json', 'headers': ['Message', 'Count', 'LastSeen'], 'title': 'Error Summary'},
                    'statistics': {'pattern': 'server-statistics.json', 'analyzer': analyzer.analyze_statistics, 'headers': ['Statistic', 'Value'], 'title': 'Server Statistics'},
                    'settings': {'pattern': 'settings.json', 'analyzer': analyzer.analyze_settings, 'headers': ['Setting', 'Value'], 'title': 'Workspace Settings'},
                    'omnichannel': {'pattern': 'omnichannel-settings.json', 'analyzer': analyzer.analyze_omnichannel, 'headers': ['Setting', 'Value'], 'title': 'Omnichannel Settings'},
                    'apps': {'pattern': 'apps-installed.json', 'analyzer': analyzer.analyze_apps, 'headers': ['Name', 'Version', 'Status'], 'title': 'Installed Apps'},
                    'logs': {'pattern': 'log.json', 'headers': ['level', 'time', 'pid', 'hostname', 'name', 'msg'], 'title': 'All Log Entries'},
                    'recommendations': {'pattern': 'log.json', 'title': 'Recommendations'},
                }
                
                files_found = {}
                for key, config in report_sections.items():
                    if key == 'settings':
                        all_settings_files = list(dump_path.glob('*settings.json'))
                        settings_file = next((f for f in all_settings_files if 'omnichannel' not in f.name.lower()), None)
                        files_found[key] = settings_file
                    else:
                        found_file = next(dump_path.glob(f"*{config['pattern']}"), None)
                        files_found[key] = found_file

                results = {}
                log_file_path = files_found.get('logs')
                
                # --- BUG FIX: Set a default min_level for the web UI ---
                log_data = analyzer.analyze_logs(log_file_path, min_level=40) if log_file_path and log_file_path.exists() else \
                           {'summary': [], 'all_errors': [], 'total_error_count': 0, 'recommendations': []}

                for key, config in report_sections.items():
                    if key in ['summary', 'logs', 'recommendations']:
                        content = log_data.get(key, []) if key != 'logs' else log_data.get('all_errors', [])
                        results[key] = {'title': config.get('title'), 'content': content, 'headers': config.get('headers'), 'total_count': log_data.get('total_error_count')}
                    else:
                        file_to_analyze = files_found.get(key)
                        content = config['analyzer'](file_to_analyze) if file_to_analyze and file_to_analyze.exists() else []
                        results[key] = {'title': config.get('title'), 'content': content, 'headers': config.get('headers')}
                
                template_path = Path(__file__).parent / 'templates' / 'report_template.html'
                html_report = reporter.generate_report(results, template_path)
                
                return html_report
        else:
            flash('Please upload a ZIP file.', 'error')
            return render_template('upload.html')
    
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
