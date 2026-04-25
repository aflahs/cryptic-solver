@echo off
REM Run unit tests for Cryptarithmetic Puzzle Solver on Windows

cd /d "%~dp0tests"
python -m unittest test_csp_solver.py -v
pause
