# Python Template

This is a template repository for creating Python projects.

## Installation

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Initial Setup

```bash
source .venv/bin/activate

# Create a new project structure in the current directory
python setup.py -t .
```

When you are satisfied with the initial structure of the project you should remove the setup virtual environment, 
templates directory, and the requirements.txt file. Then rebuild the .venv directory with the project dependencies.

```bash
deactivate
rm -rf .venv
rm -rf templates
rm -f requirements.txt
python3.13 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install flit invoke
invoke install
```
