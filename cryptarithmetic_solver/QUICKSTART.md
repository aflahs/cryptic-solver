# Quick Start Guide - 5 Minutes to Solving Puzzles 🚀

## Step 1: Check Python (30 seconds)

```bash
python3 --version
# You should see: Python 3.7 or higher
```

## Step 2: Navigate to Project (30 seconds)

```bash
cd cryptarithmetic_solver
```

## Step 3: Choose Your Mode

### 🎮 Option A: Interactive GUI (Recommended)

```bash
cd src
python3 main.py --gui
```

**Then:**
1. Click an example button (e.g., "SEND + MORE = MONEY")
2. Click "Solve Puzzle"
3. View the solution mapping and arithmetic verification
4. Click "Next" to see more solutions (if any)

### 💻 Option B: Command Line

```bash
cd src
python3 main.py "SEND + MORE = MONEY"
```

**Output:**
```
Puzzle: SEND + MORE = MONEY
Unique letters: D, E, M, N, O, R, S, Y
Number of solutions: 1

=== Solution ===
Mapping:
  D = 7, E = 5, M = 1, N = 6
  O = 0, R = 8, S = 9, Y = 2

Equation: 9567 + 1085 = 10652 ✓
```

### 🧪 Option C: Run Tests

```bash
python3 -m unittest tests.test_csp_solver.py -v
```

**Expected:** 15/15 tests passing ✅

---

## 🎯 Try These Puzzles

```bash
python3 main.py "SEND + MORE = MONEY"
python3 main.py "CROSS + ROADS = DANGER"
python3 main.py "A + B = C"
python3 main.py "HELLO + WORLD = GREET"
```

---

## 📚 Next Steps

- **Want details?** Read [README.md](README.md)
- **Need setup help?** See [SETUP_AND_EXECUTION.md](SETUP_AND_EXECUTION.md)
- **More puzzles?** Check [EXAMPLES.md](EXAMPLES.md)
- **Understand the algorithm?** Read [docs/algorithm_explanation.md](docs/algorithm_explanation.md)

---

## ⚡ Common Issues

| Issue | Solution |
|-------|----------|
| GUI doesn't open | Try CLI instead: `python3 main.py "SEND + MORE = MONEY"` |
| "ModuleNotFoundError" | Ensure you're in the `src` directory: `cd src` |
| No solutions found | Check puzzle syntax (spaces around operators) |
| Slow solving | Large puzzles (9+ letters) take time - be patient! |

---

## ✅ You're Ready!

Congratulations! You can now:
- ✅ Solve cryptarithmetic puzzles
- ✅ Find all valid solutions
- ✅ Understand CSP techniques
- ✅ Explore AI problem-solving

**Happy puzzle solving! 🎉**

---

For more information, see the full README.md
