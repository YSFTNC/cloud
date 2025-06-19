#!/bin/bash

# Navigate to the server directory
cd "$(dirname "$0")"

# Install dependencies
echo "Installing dependencies..."
npm install

# Verify express installation
if [ -d "node_modules/express" ]; then
    echo "Express module is installed correctly"
else
    echo "Error: Express module is not installed"
    exit 1
fi

# Start the application
echo "Starting the application..."
npm start 