#!/bin/bash

echo "Building Vortex Downloader executable..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed or not in PATH"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
    echo "Virtual environment created."
    echo ""
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to activate virtual environment"
    exit 1
fi

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip > /dev/null 2>&1

# Install/upgrade dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

# Build executable with PyInstaller
echo ""
echo "Creating executable..."
pyinstaller --onefile --console --name "VortexDownloader" main.py

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Build failed!"
    exit 1
fi

# Deactivate virtual environment (optional, script will end anyway)
deactivate > /dev/null 2>&1

echo ""
echo "========================================"
echo "Build successful!"
echo "Executable location: dist/VortexDownloader"
echo "========================================"
echo ""

