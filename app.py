# app.py
from flask import Flask, render_template, request, flash
import os
import tempfile
import zipfile
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from typing import Optional

# Import the analysis and reporting functions
import analyzer
from config import config
from utils import (
    validate_zip_file, safe_extract_zip, find_dump_path, 
    get_safe_filename, setup_logging, ValidationError, LOG_LEVEL_NAMES
)

def create_app(config_name=None):
    """Application factory pattern."""
    if config_name is None:
        config_name = os.environ.get('FLASK_ENV', 'development')
    
    app = Flask(__name__, template_folder='templates')
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    setup_logging()
    
    # Register routes
    register_routes(app)
    
    return app

def register_routes(app):
    """Register application routes."""
    
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
                safe_filename = get_safe_filename(file.filename)
                min_level = int(request.form.get('log_level', 40))  # Get log level, default to 40
                
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_path = Path(temp_dir)
                    file_path = temp_path / safe_filename
                    file.save(file_path)

                    try:
                        # Validate the ZIP file for security
                        validate_zip_file(
                            file_path, 
                            app.config['MAX_CONTENT_LENGTH'],
                            app.config['MAX_EXTRACTED_SIZE']
                        )
                        
                        # Safely extract the ZIP file
                        safe_extract_zip(
                            file_path, 
                            temp_path, 
                            app.config['MAX_SINGLE_FILE_SIZE']
                        )
                        
                    except ValidationError as e:
                        flash(f"Upload failed: {str(e)}", "error")
                        return render_template('upload.html')

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
                    for key, config_section in report_sections.items():
                        if key == 'settings':
                            all_settings_files = list(dump_path.glob('*settings.json'))
                            settings_file = next((f for f in all_settings_files if 'omnichannel' not in f.name.lower()), None)
                            files_found[key] = settings_file
                        else:
                            found_file = next(dump_path.glob(f"*{config_section['pattern']}"), None)
                            files_found[key] = found_file

                    results = {}
                    log_file_path = files_found.get('logs')
                    
                    log_data = analyzer.analyze_logs(log_file_path, min_level=min_level) if log_file_path and log_file_path.exists() else \
                               {'summary': [], 'all_errors': [], 'total_error_count': 0, 'recommendations': [], 'chart_data_timeline': {}, 'chart_data_severity': {}, 'timeline_full_logs': {}}

                    for key, config_section in report_sections.items():
                        if key == 'summary':
                            results[key] = {'title': config_section.get('title'), 'content': log_data.get('summary', []), 'headers': config_section.get('headers')}
                        elif key == 'recommendations':
                             results[key] = {'title': config_section.get('title'), 'content': log_data.get('recommendations', [])}
                        elif key == 'logs':
                            results[key] = {
                                'title': config_section.get('title'),
                                'content': log_data.get('all_errors', []),
                                'headers': config_section.get('headers'),
                                'total_count': log_data.get('total_error_count'),
                                'chart_data_timeline': log_data.get('chart_data_timeline', {}),
                                'chart_data_severity': log_data.get('chart_data_severity', {}),
                                'timeline_full_logs': log_data.get('timeline_full_logs', {})
                            }
                        else:
                            file_to_analyze = files_found.get(key)
                            content = config_section['analyzer'](file_to_analyze) if file_to_analyze and file_to_analyze.exists() else []
                            results[key] = {'title': config_section.get('title'), 'content': content, 'headers': config_section.get('headers')}
                    
                    template_dir = Path(__file__).parent / 'templates'
                    env = Environment(loader=FileSystemLoader(template_dir), autoescape=True)
                    template = env.get_template('report_template.html')
                    
                    html_report = template.render(
                        results=results, 
                        log_level_name=LOG_LEVEL_NAMES.get(min_level, str(min_level)),
                        version=app.config['VERSION']
                    )
                    
                    return html_report
            else:
                flash('Please upload a ZIP file.', 'error')
                return render_template('upload.html')
        
        return render_template('upload.html')

# Initialize the Flask application
app = create_app()

if __name__ == '__main__':
    # For development only - in production, use Gunicorn
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV', 'production') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)
# To run the application, use the command: python app.py
# Access it in your browser at http://127.0.0.1:5000/
# Ensure you have the required templates in the 'templates' directory
# and the analyzer module with the necessary functions defined. 
# Make sure to install Flask and other dependencies before running the app.
# Note: The analyzer module should contain the functions used for analyzing the JSON files.

