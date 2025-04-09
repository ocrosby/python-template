import os
import shutil
from datetime import datetime
import click
from jinja2 import Environment, FileSystemLoader
from InquirerPy import prompt

VERSION = '0.1.0'

def render_template(template_path, output_path, context):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    content = template.render(context)
    with open(output_path, 'w') as file:
        file.write(content)

@click.command()
@click.option('--target-dir', '-t', default='.', help='Target directory for generated files (default: current directory).')
def main(target_dir: str):
    """Setup script to generate project files based on templates."""
    # Delete the target directory if it exists
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)

    questions = [
        {"type": "input", "name": "project_name", "message": "Enter the project name:", "default": "My Project"},
        {"type": "input", "name": "project_owner", "message": "Enter the GitHub project owner name:", "default": "fflintstone"},
        {"type": "input", "name": "author", "message": "Enter the author name:", "default": "Fred Flintstone"},
        {"type": "input", "name": "description", "message": "Enter the project description:", "default": "A sample project"},
        {"type": "input", "name": "license", "message": "Enter the license type (e.g., MIT):", "default": "MIT"},
        {"type": "input", "name": "email", "message": "Enter the author email:", "default": "fred.flintstone@example.com"},
    ]

    context = prompt(questions)

    # Store both original and modified project names
    context['version'] = VERSION
    context['year'] = str(datetime.now().year) # Set the current year dynamically
    context['module_name'] = context['project_name'].lower().replace(" ", "-")  # For PyPI
    context['package_name'] = context['project_name'].lower().replace(" ", "_")  # For internal use

    templates_to_render = {
        'templates/tests/__init__.py.jinja2': 'tests/__init__.py',
        'templates/tests/conftest.py.jinja2': 'tests/conftest.py',
        'templates/tests/test_example.py.jinja2': 'tests/test_example.py',
        'templates/.flake8.jinja2': '.flake8',
        'templates/.gitignore.jinja2': '.gitignore',
        'templates/.isort.cfg.jinja2': '.isort.cfg',
        'templates/.pylintrc.jinja2': '.pylintrc',
        'templates/commitlint.config.js.jinja2': 'commitlint.config.js',
        'templates/eslint.config.cjs.jinja2': 'eslint.config.cjs',
        'templates/LICENSE.jinja2': 'LICENSE',
        'templates/mypy.ini.jinja2': 'mypy.ini',
        'templates/package.json.jinja2': 'package.json',
        'templates/pyproject.toml.jinja2': 'pyproject.toml',
        'templates/pytest.ini.jinja2': 'pytest.ini',
        'templates/README.md.jinja2': 'README.md',
        'templates/release.config.js.jinja2': 'release.config.js',
        'templates/update_version.py.jinja2': 'update_version.py',
        'templates/app/__init__.py.jinja2': os.path.join(context.get('package_name'), '__init__.py'),
        'templates/app/main.py.jinja2': os.path.join(context.get('package_name'), 'main.py'),
        # Add other template files here
    }

    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Ensure the tests directory exists
    tests_dir = os.path.join(target_dir, 'tests')
    os.makedirs(tests_dir, exist_ok=True)

    # Ensure the app directory exists
    app_dir = os.path.join(target_dir, context.get('package_name'))
    os.makedirs(app_dir, exist_ok=True)

    for template_path, output_path in templates_to_render.items():
        # AAdjust the output path to be relative to the target directory
        output_path = os.path.join(target_dir, output_path)
        render_template(template_path, output_path, context)

    # Create the package directory using the internal package name
    package_dir = os.path.join(target_dir, context['package_name'])
    os.makedirs(package_dir, exist_ok=True)

    # Create an empty __init__.py file in the package directory
    init_file_path = os.path.join(package_dir, '__init__.py')
    with open(init_file_path, 'w') as init_file:
        pass  # Create an empty file

    print(f"Setup complete! Files generated in : {os.path.abspath(target_dir)}")

if __name__ == "__main__":
    main()
