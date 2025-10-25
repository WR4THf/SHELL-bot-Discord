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

echo Starting bot...
python bot.py
pause
