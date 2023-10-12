#!/bin/bash

# Install Python 3.10
sudo apt update
sudo apt install python3.10

# Create a virtual environment with Python 3.10
python3.10 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Install the libraries from the requirements.txt file
pip install -r requirements.txt

echo "Python 3.10 installed, virtual environment created, and libraries from requirements.txt are installed."
