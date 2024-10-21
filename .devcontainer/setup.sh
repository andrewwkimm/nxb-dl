#!/bin/bash

# Get an environment variable's value
get_env_value() {
    local key="$1"
    local value

    if [[ -f .env ]]; then
        # Check if the key exists in the .env file
        value=$(grep "^$key=" .env | cut -d '=' -f2)
    fi

    echo "$value"
}

# Try to get Git username and email from .env file
git_username=$(get_env_value "GIT_USERNAME")
git_email=$(get_env_value "GIT_EMAIL")

# Prompt for username and/or email if not found
if [ -z "$git_username" ]; then
    read -p "Enter your Git username: " git_username
fi

if [ -z "$git_email" ]; then
    read -p "Enter your Git email: " git_email
fi

# Check if GIT_USERNAME and GIT_EMAIL already exist in .env file
if ! (grep -q "^GIT_USERNAME=" .env 2>/dev/null && grep -q "^GIT_EMAIL=" .env 2>/dev/null); then
    # Ask if user wants to write Git credentials to .env file
    write_to_env_file=false
    read -p "Write Git credentials to .env file? (y/n): " response
    case $response in
        y|Y) write_to_env_file=true ;;
    esac

    if $write_to_env_file; then
        if [ ! -f .env ]; then
            touch .env
        fi

        # Remove existing GIT_USERNAME and GIT_EMAIL lines
        sed -i "/^GIT_USERNAME=/d" .env
        sed -i "/^GIT_EMAIL=/d" .env

        # Append GIT_USERNAME and GIT_EMAIL to the end of the file
        echo "GIT_USERNAME=$git_username" >> .env
        echo "GIT_EMAIL=$git_email" >> .env
        echo "Updated .env file with Git credentials."
    fi
fi

# Configure baseline git settings
git config --global core.editor "code --wait"
git config --global --add safe.directory $(pwd)
git config --global user.email "$git_email"
git config --global user.name "$git_username"

# Change ownership of the workspace to vscode user
chown -R vscode:vscode $(pwd)

# Setup environment and activate poetry's virtual environment
make setup
