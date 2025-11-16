#!/bin/bash

echo "Setting up development environment..."
echo ""

if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment."
        exit 1
    fi
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Upgrading pip..."
pip install --upgrade pip -q

echo "Installing dependencies..."
if ! pip install -r requirements.txt -q; then
    echo "Failed to install dependencies."
    exit 1
fi

echo ""
echo "Installing pre-commit hooks..."
pre-commit install

if [ $? -ne 0 ]; then
    echo "Failed to install pre-commit hooks."
    exit 1
fi

echo ""
echo "Testing pre-commit hooks on all files..."
pre-commit run --all-files

echo ""
echo "Setup complete!"
echo ""
echo "To activate the virtual environment, run:"
echo "  source venv/bin/activate"
echo ""
