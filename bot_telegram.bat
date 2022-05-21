@echo off

call %~dp0math_bot\venv\Scripts\activate

cd %~dp0math_bot

set TOKEN=5327779582:AAETGTDleTBFNt9rSoxh9Cw7wnMP9s9urAo

python bot_telegram.py

pause