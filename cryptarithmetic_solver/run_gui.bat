@echo off
REM Launch the Cryptarithmetic Puzzle Solver GUI on Windows

cd /d "%~dp0src"
python main.py --gui
pause
