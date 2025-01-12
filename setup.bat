@echo off
color a
echo Installing required libraries for the script...
pip install -r requirements.txt > NUL 2>&1
cls
start /B start.bat