import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from InquirerPy import prompt

VERSION = '0.1.0'

def render_template(template_path, output_path, context):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    content = template.render(context)
    with open(output_path, 'w') as file:
        file.write(content)

def main():
    questions = [
        {"type": "input", "name": "project_name", "message": "Enter the project name:"},
        {"type": "input", "name": "author", "message": "Enter the author name:"},
        {"type": "input", "name": "description", "message": "Enter the project description:"},
        {"type": "input", "name": "license", "message": "Enter the license type (e.g., MIT):"},
        {"type": "input", "name": "email", "message": "Enter the author email:"},
    ]

    context = prompt(questions)

    # Store both original and modified project names
    context['version'] = VERSION
    context['year'] = str(datetime.now().year) # Set the current year dynamically
    context['module_name'] = context['project_name'].lower().replace(" ", "-")  # For PyPI
    context['package_name'] = context['project_name'].lower().replace(" ", "_")  # For internal use

    templates_to_render = {
        'templates/LICENSE.jinja2': 'LICENSE',
        'templates/package.json.jinja2': 'package.json',
        'templates/pyproject.toml.jinja2': 'pyproject.toml',
        'templates/pytest.ini.jinja2': 'pytest.ini',
        'templates/README.md.jinja2': 'README.md',
        'templates/release.config.js.jinja2': 'release.config.js',
        'templates/update_version.py.jinja2': 'update_version.py',
        # Add other template files here
    }

    for template_path, output_path in templates_to_render.items():
        render_template(template_path, output_path, context)

    print("Setup complete!")

if __name__ == "__main__":
    main()
