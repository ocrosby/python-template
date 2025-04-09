# Python Template

This is a template repository for creating Python projects.

From a repository created from this template, you can create a new project by following these steps:

## Step 1. Create a New Repository from this Template in GitHub

## Step 2. Clone the New Repository

```bash
git clone https://github.com/<your-github-user>/<your-repo-name>.git
```

## Step 3. Initial Setup

```bash
cd <your-repo-name>
./setup.sh
```

## Step 4. Commit and Push

Please be careful to not attempt to commit and push back to the template repository.
These steps are intended to be run in a new repository created from this template.

```bash
# Create a new feature branch for your changes
git checkout -b feature/init

# Add all files to the staging area
git add .

# Commit the changes with a message
git commit -m "chore: initial setup"

# Push the changes to the new repository
git push --set-upstream origin feature/init
```

Yes, that's all you need to do.
