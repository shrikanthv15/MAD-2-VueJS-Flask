#!/bin/bash

source .venv/scripts/activate

echo "Exporting Flask app..."
export FLASK_APP=hello.py
export FLASK_ENV=development
export FLASK_DEBUG=True

# Run Flask
echo "Running Flask..."
flask run

