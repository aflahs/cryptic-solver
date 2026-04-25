# Setup and Execution Guide

## System Requirements

- **Python Version:** 3.7 or higher
- **Operating System:** Windows, macOS, or Linux
- **Dependencies:** None! Only Python standard library is used
- **RAM:** Minimum 512 MB (1 GB recommended)
- **Storage:** 5 MB

## Installation Steps

### Step 1: Verify Python Installation

Check if Python 3 is installed:

**Linux/macOS:**
```bash
python3 --version
```

**Windows (Command Prompt):**
```cmd
python --version
```

You should see output like: `Python 3.9.0` (version 3.7 or higher)

If Python is not installed, download from: https://www.python.org/downloads/

### Step 2: Navigate to Project Directory

```bash
cd cryptarithmetic_solver
```

### Step 3: Verify Project Structure

Confirm the folder structure:

```
cryptarithmetic_solver/
├── src/
│   ├── main.py
│   ├── csp_solver.py
│   └── gui.py
├── tests/
│   └── test_csp_solver.py
├── docs/
│   └── algorithm_explanation.md
├── README.md
└── EXAMPLES.md
```

If any files are missing, they can be regenerated from the provided code.

---

## Execution Methods

### Method 1: GUI Application (Recommended for Users)

The GUI provides an interactive interface for solving cryptarithmetic puzzles.

#### On Linux/macOS:

```bash
chmod +x run_gui.sh    # Make script executable (first time only)
./run_gui.sh
```

Or directly:
```bash
cd src
python3 main.py --gui
```

#### On Windows:

Double-click `run_gui.bat` or run in Command Prompt:
```cmd
cd src
python main.py --gui
```

**Expected Output:**
A window titled "Cryptarithmetic Puzzle Solver (CSP Approach)" should open with:
- Input field for equations
- Example puzzle buttons
- Solution display area
- Navigation buttons

#### GUI Usage:

1. **Enter a Puzzle:** Type or select an example puzzle
2. **Solve:** Click "Solve Puzzle" button
3. **View Results:** See mapping and arithmetic verification
4. **Navigate:** Use "Previous" and "Next" buttons for multiple solutions
5. **Clear:** Click "Clear" to reset

**Example Puzzles:**
- `SEND + MORE = MONEY`
- `CROSS + ROADS = DANGER`
- `HELLO + WORLD = GREET`
- `TWELVE + TWELVE = TWENTY`

---

### Method 2: Command Line (CLI)

Perfect for quick solving and scripting.

#### On Linux/macOS:

```bash
cd src
python3 main.py "SEND + MORE = MONEY"
```

#### On Windows:

```cmd
cd src
python main.py "SEND + MORE = MONEY"
```

**Expected Output:**
```
Puzzle: SEND + MORE = MONEY
Unique letters: D, E, M, N, O, R, S, Y
Number of solutions: 1

=== Solution ===
Mapping:
  D = 7
  E = 5
  ...
```

#### CLI Examples:

**Single puzzle:**
```bash
python3 main.py "SEND + MORE = MONEY"
```

**Another puzzle:**
```bash
python3 main.py "CROSS + ROADS = DANGER"
```

**Show help:**
```bash
python3 main.py --help
```

**Launch GUI from CLI:**
```bash
python3 main.py --gui
```

---

### Method 3: Run Tests

Verify that the solver works correctly with comprehensive unit tests.

#### On Linux/macOS:

```bash
chmod +x run_tests.sh   # Make script executable (first time only)
./run_tests.sh
```

Or directly:
```bash
cd tests
python3 -m unittest test_csp_solver.py -v
```

#### On Windows:

Double-click `run_tests.bat` or run:
```cmd
cd tests
python -m unittest test_csp_solver.py -v
```

**Expected Output:**
```
test_cross_roads_danger ... ok
test_format_solution ... ok
test_no_leading_zeros ... ok
...
Ran 15 tests in 35.8s
OK
```

#### Run Specific Test:

```bash
python3 -m unittest tests.test_csp_solver.TestCryptarithmeticCSP.test_send_more_money -v
```

---

### Method 4: Programmatic Usage

Use the solver in your own Python code:

```python
import sys
sys.path.insert(0, 'src')

from csp_solver import CryptarithmeticCSP

# Create and solve
solver = CryptarithmeticCSP("SEND + MORE = MONEY")
solutions = solver.solve()

# Display results
for i, solution in enumerate(solutions, 1):
    print(f"\nSolution {i}:")
    print(solver.format_solution(solution))
```

Save as `solve_example.py` and run:
```bash
cd cryptarithmetic_solver
python3 solve_example.py
```

---

## File Descriptions

### Core Files

| File | Purpose |
|------|---------|
| `src/main.py` | Entry point for CLI and GUI |
| `src/csp_solver.py` | CSP solver implementation |
| `src/gui.py` | GUI application using tkinter |

### Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Main documentation and overview |
| `EXAMPLES.md` | Puzzle examples and solutions |
| `docs/algorithm_explanation.md` | Detailed algorithm explanation |
| `SETUP_AND_EXECUTION.md` | This file |

### Testing Files

| File | Purpose |
|------|---------|
| `tests/test_csp_solver.py` | Unit tests (15 test cases) |

### Utility Scripts

| File | Purpose |
|------|---------|
| `run_gui.sh` / `run_gui.bat` | Quick launcher for GUI |
| `run_tests.sh` / `run_tests.bat` | Quick launcher for tests |
| `requirements.txt` | Python dependencies (none!) |

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'gui'"

**Solution:** Ensure you're running from the correct directory

```bash
cd src
python3 main.py --gui
```

### Issue: GUI window doesn't appear

**Possible causes:**
1. tkinter not installed (usually included with Python)
2. Display server issues (Linux with SSH)

**Solution:**
- On Ubuntu/Debian: `sudo apt-get install python3-tk`
- On Fedora: `sudo dnf install python3-tkinter`
- Try CLI mode instead: `python3 main.py "SEND + MORE = MONEY"`

### Issue: "SyntaxError: invalid syntax"

**Cause:** Python version < 3.7

**Solution:** Upgrade Python to 3.7+
```bash
python3 --version  # Check version
```

### Issue: Tests fail with "No module named 'csp_solver'"

**Solution:** Run tests from correct directory
```bash
cd cryptarithmetic_solver  # Root directory
python3 -m unittest tests.test_csp_solver -v
```

### Issue: "Too many unique letters" error

**Cause:** Puzzle has more than 10 unique letters

**Solution:** Use a simpler puzzle or one with repeated letters

**Example:**
- ✗ Bad: `ABCDEFGHIJK + L = M` (12 unique letters)
- ✓ Good: `SEND + MORE = MONEY` (8 unique letters)

### Issue: "No solutions found"

**Possible causes:**
1. Invalid equation syntax
2. Mathematically impossible puzzle
3. Typo in letters

**Verify:**
```bash
# Check syntax is correct
python3 main.py "SEND + MORE = MONEY"  # Should work

# Try another example
python3 main.py "CROSS + ROADS = DANGER"
```

### Issue: Slow solving (>10 seconds)

**Cause:** Puzzle with many unique letters (8-10)

**Note:** This is expected behavior for complex puzzles
- SEND + MORE = MONEY: ~50-100ms
- CROSS + ROADS = DANGER: ~100-200ms
- Complex puzzles: 1-5 seconds

**Solution:** Be patient or simplify the puzzle

---

## Platform-Specific Instructions

### Windows

#### Using GUI:
1. Navigate to project folder in File Explorer
2. Double-click `run_gui.bat`
3. A window should open

Or use Command Prompt:
```cmd
cd src
python main.py --gui
```

#### Using CLI:
```cmd
cd src
python main.py "SEND + MORE = MONEY"
```

#### Using Tests:
```cmd
cd tests
python -m unittest test_csp_solver.py -v
```

### macOS

#### Using GUI:
```bash
cd src
python3 main.py --gui
```

#### Using CLI:
```bash
cd src
python3 main.py "SEND + MORE = MONEY"
```

#### Using Tests:
```bash
cd tests
python3 -m unittest test_csp_solver.py -v
```

### Linux

#### Using GUI:
```bash
cd src
python3 main.py --gui
```

#### Using CLI:
```bash
cd src
python3 main.py "SEND + MORE = MONEY"
```

#### Using Tests:
```bash
cd tests
python3 -m unittest test_csp_solver.py -v
```

#### Install tkinter (if needed):
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch
sudo pacman -S tk
```

---

## Performance Benchmarks

### Solving Time (Typical)

Run on standard hardware:

```bash
cd src
python3 main.py "A + B = C"           # < 1ms
python3 main.py "SEND + MORE = MONEY" # ~50-100ms
python3 main.py "CROSS + ROADS = DANGER" # ~100-200ms
```

### Test Execution Time

```bash
python3 -m unittest tests.test_csp_solver -v
# Ran 15 tests in ~35 seconds
```

---

## Next Steps

1. **Try Examples:** Run the GUI or CLI with provided puzzles
2. **Read Documentation:** See README.md for detailed information
3. **Explore Algorithm:** Check docs/algorithm_explanation.md
4. **Run Tests:** Verify everything works with `run_tests.sh`
5. **Create Puzzles:** Design your own cryptarithmetic puzzles

---

## Additional Resources

- **README.md:** Complete project documentation
- **EXAMPLES.md:** More puzzles and usage examples
- **docs/algorithm_explanation.md:** Deep dive into CSP algorithm
- **Source Code:** Well-commented implementation

---

## Support

### Reporting Issues

If you encounter problems:

1. Check this troubleshooting section
2. Review the error message carefully
3. Try running tests: `python3 -m unittest tests.test_csp_solver -v`
4. Verify Python version: `python3 --version`

### Getting Help

- Read the README.md for comprehensive documentation
- Check EXAMPLES.md for usage patterns
- Review algorithm_explanation.md for technical details
- Examine source code comments for implementation details

---

## Quick Reference

### Commands

| Task | Command |
|------|---------|
| Launch GUI | `cd src && python3 main.py --gui` |
| Solve puzzle (CLI) | `cd src && python3 main.py "PUZZLE"` |
| Run tests | `cd tests && python3 -m unittest test_csp_solver.py -v` |
| Check Python version | `python3 --version` |
| Show help | `cd src && python3 main.py --help` |

### Files to Know

| File | Why Important |
|------|---|
| `src/main.py` | Start here for execution |
| `src/csp_solver.py` | Core algorithm implementation |
| `README.md` | Full project documentation |
| `tests/test_csp_solver.py` | Verify everything works |

---

## Conclusion

You're ready to use the Cryptarithmetic Puzzle Solver! Start with the GUI for an interactive experience or use the CLI for quick solving. Check the EXAMPLES.md file for inspiration on what puzzles to try.

Happy puzzle solving! 🎯
