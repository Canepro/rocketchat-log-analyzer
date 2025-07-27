# reporter.py
from jinja2 import Environment, FileSystemLoader
from pathlib import Path

def generate_report(results, template_path: Path):
    """
    Generates an HTML report from the analysis results and returns it as a string.
    
    v2.0 Change: Instead of writing to an output file, this function now
    loads the template and returns the rendered HTML content.
    """
    
    template_dir = template_path.parent
    template_file = template_path.name
    
    # Set up the Jinja2 environment to load the template
    env = Environment(loader=FileSystemLoader(template_dir), autoescape=True)
    template = env.get_template(template_file)

    # Render the template with the analysis results
    html_content = template.render(results=results)
    
    return html_content