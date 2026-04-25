#!/bin/bash
# Run the unit tests for Cryptarithmetic Puzzle Solver

cd "$(dirname "$0")/tests"
python3 -m unittest test_csp_solver.py -v
