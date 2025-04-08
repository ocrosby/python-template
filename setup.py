import os
from jinja2 import Environment, FileSystemLoader

def render_template(template_path, output_path, context):
    env = Environment(loader=FileSystemLoader(os.path.dirname(template_path)))
    template = env.get_template(os.path.basename(template_path))
    content = template.render(context)
    with open(output_path, 'w') as file:
        file.write(content)

def main():
    project_name = input("Enter the project name: ")
    author_name = input("Enter the author name: ")
    description = input("Enter the project description: ")

    context = {
        "project_name": project_name,
        "author_name": author_name,
        "project_description": description
    }

    templates_to_render = {
        'README.md.jinja': 'README.md',
        'setup.py.jinja': 'setup.py',
        # Add other template files here
    }

    for template_path, output_path in templates_to_render.items():
        render_template(template_path, output_path, context)

    print("Setup complete!")

if __name__ == "__main__":
    main()