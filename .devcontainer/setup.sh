#!/bin/bash

# Configure baseline git settings
git config --global --add safe.directory $(pwd)
git config --global user.email "andrewkimka@gmail.com"
git config --global user.name "Andrew Kim"

# Setup environment
make setup
