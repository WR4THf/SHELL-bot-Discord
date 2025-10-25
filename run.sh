#!/bin/bash

echo "Starting Discord Terminal Bot..."

if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

if [ ! -f ".env" ]; then
    echo "Warning: .env file not found!"
    echo "Please create .env file from .env.example"
    cp .env.example .env
    echo "Created .env file. Please edit it with your Discord token before running again."
    exit 1
fi

echo "Starting bot..."
python bot.py
