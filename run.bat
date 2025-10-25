@echo off
title Discord Terminal Bot Launcher
echo Starting Discord Terminal Bot...

if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

if not exist ".env" (
    echo Warning: .env file not found!
    echo Please create .env file from .env.example
    copy .env.example .env
    echo Created .env file. Please edit it with your Discord token before running again.
    pause
    exit /b 1
)

echo Starting bot...
python bot.py
pause
