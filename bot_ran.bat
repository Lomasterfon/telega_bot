@echo off

call %~dp0telega_bot\venv\Scripts\activate


cd %~dp0telega_bot

set TOKEN=***

python telega_bot.py


pause
