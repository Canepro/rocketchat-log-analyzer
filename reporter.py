# reporter.py
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate_report(results, output_path: Path):
    """Generates an HTML report from the analysis results."""
    
    template_dir = Path(__file__).parent / 'templates'
    env = Environment(loader=FileSystemLoader(template_dir), autoescape=True)
    template = env.get_template('report_template.html')

    html_content = template.render(results=results)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
        
    return str(output_path)