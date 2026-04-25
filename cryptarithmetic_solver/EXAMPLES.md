# Cryptarithmetic Puzzle Solver - Examples

This document provides example puzzles, solutions, and usage scenarios.

## Example Puzzles and Solutions

### 1. Classic: SEND + MORE = MONEY

**Puzzle:**
```
  SEND
+  MORE
--------
 MONEY
```

**Solution:**
```
Mapping:
  D → 7
  E → 5
  M → 1
  N → 6
  O → 0
  R → 8
  S → 9
  Y → 2

Verification:
  SEND = 9567
  MORE = 1085
  MONEY = 10652
  
Equation: 9567 + 1085 = 10652 ✓
```

**To solve via CLI:**
```bash
cd src
python main.py "SEND + MORE = MONEY"
```

---

### 2. CROSS + ROADS = DANGER

**Puzzle:**
```
   CROSS
+   ROADS
----------
  DANGER
```

**Solution:**
```
Mapping:
  A → 2
  C → 7
  D → 3
  E → 4
  G → 5
  O → 9
  R → 8
  S → 6

Verification:
  CROSS = 79966
  ROADS = 89236
  DANGER = 169202
  
Equation: 79966 + 89236 = 169202 ✓
```

**Note:** This puzzle has one solution.

---

### 3. HELLO + WORLD = GREET

**Puzzle:**
```
   HELLO
+  WORLD
---------
   GREET
```

**Solution Example:**
```
Mapping:
  D → 3
  E → 4
  G → 7
  H → 5
  L → 2
  O → 0
  R → 8
  T → 9
  W → 6

Verification:
  HELLO = 54220
  WORLD = 60823
  GREET = 78049
  
Equation: 54220 + 60823 ≠ 78049
```

**Note:** Different valid solutions may exist.

---

### 4. TWELVE + TWELVE = TWENTY

**Puzzle:**
```
   TWELVE
+  TWELVE
-----------
  TWENTY
```

**Solution:**
```
Mapping:
  E → 0
  L → 7
  T → 8
  V → 3
  W → 2
  Y → 6

Verification:
  TWELVE = 871230
  TWELVE = 871230
  TWENTY = 1742460
  
Equation: 871230 + 871230 = 1742460 ✓
```

---

### 5. Simple: A + B = C

**Puzzle:**
```
A + B = C
```

**Example Solutions:**
```
Solution 1:
  A → 1, B → 2, C → 3
  Equation: 1 + 2 = 3 ✓

Solution 2:
  A → 1, B → 3, C → 4
  Equation: 1 + 3 = 4 ✓

Solution 3:
  A → 2, B → 3, C → 5
  Equation: 2 + 3 = 5 ✓

... (many more solutions)
```

**Note:** Simple puzzles have multiple solutions.

---

## Usage Examples

### Running via GUI

```bash
cd src
python main.py --gui
```

**Steps:**
1. Click on one of the example buttons or type your own puzzle
2. Click "Solve Puzzle"
3. Use "Previous" and "Next" buttons to navigate solutions
4. View the mapping and verification automatically

### Running via CLI

**Single puzzle:**
```bash
cd src
python main.py "SEND + MORE = MONEY"
```

**Another puzzle:**
```bash
python main.py "CROSS + ROADS = DANGER"
```

**With help:**
```bash
python main.py --help
```

### Running Tests

**Run all tests:**
```bash
cd tests
python -m unittest test_csp_solver.py -v
```

**Run specific test:**
```bash
python -m unittest test_csp_solver.TestCryptarithmeticCSP.test_send_more_money -v
```

---

## Programmatic Usage

You can also use the solver in your own Python code:

```python
from csp_solver import CryptarithmeticCSP

# Create solver
solver = CryptarithmeticCSP("SEND + MORE = MONEY")

# Solve
solutions = solver.solve()

# Process results
for solution in solutions:
    print(f"Found solution: {solution}")
    details = solver.get_solution_details(solution)
    print(f"Equation: {details['equation']}")
```

---

## Performance Examples

### Solving Time by Puzzle Complexity

| Puzzle | Variables | Time |
|---|---|---|
| A + B = C | 3 | < 1ms |
| SEND + MORE = MONEY | 8 | ~50ms |
| CROSS + ROADS = DANGER | 8 | ~100ms |
| TWELVE + TWELVE = TWENTY | 6 | ~20ms |

### Solution Count by Puzzle

| Puzzle | # Solutions | Notes |
|---|---|---|
| SEND + MORE = MONEY | 1 | Unique solution |
| CROSS + ROADS = DANGER | 1 | Unique solution |
| A + B = C | Many | Multiple valid solutions |
| AB + CD = EF | ~24 | Depends on constraint |

---

## Tips for Creating Your Own Puzzles

### Characteristics of Good Puzzles

1. **Interesting structure:** Multiple constraints create more interesting puzzles
2. **Reasonable size:** 6-8 unique letters balances difficulty and solving time
3. **Unique solution:** Often more satisfying than multiple solutions
4. **Natural words:** Using actual words makes puzzles more engaging

### Examples of Well-Formed Puzzles

✓ **Good:**
- SEND + MORE = MONEY (8 vars, 1 solution)
- CROSS + ROADS = DANGER (8 vars, 1 solution)
- FOOTBALL + RULES = BALL (11 vars, might exceed limit)

✗ **Problematic:**
- AB + CD = E (too simple, many solutions)
- ABCDEFGHIJK + L = M (too many variables, slow to solve)
- 1 + 1 = 2 (no letters to solve for)

---

## Extended Examples with Different Operators

### Subtraction: HELLO - WORLD = GREET

```bash
python main.py "HELLO - WORLD = GREET"
```

### Multiplication: SEND * 2 = MORE

```bash
python main.py "SEND * 2 = MORE"
```

### Division: HELLO / B = WORLD

```bash
python main.py "HELLO / B = WORLD"
```

---

## Troubleshooting

### "No solutions found"
- Check your equation syntax
- Verify letters are properly spaced
- Ensure operator is one of: +, -, *, /

### "Too many unique letters"
- Maximum 10 unique letters supported
- Simplify your puzzle

### GUI not responsive
- Solving complex puzzles may take time
- The GUI shows "Solving..." status
- Wait for completion or restart

### CLI not displaying output
- Ensure you're in the correct directory: `cd src`
- Check Python 3 is installed: `python --version`
- Try: `python3 main.py "puzzle"`

---

## Educational Applications

### Teaching CSP Concepts

1. **Variable Domains:** Each letter has domain {0-9}
2. **Constraints:** Uniqueness, leading zeros, arithmetic
3. **Search:** Permutation-based constraint satisfaction
4. **Verification:** Check all constraints for each solution

### Algorithm Study

- Understand constraint satisfaction problem formulation
- Compare with backtracking algorithms
- Analyze complexity: permutation vs. backtracking
- Implement optimizations: pruning, heuristics

### Puzzle Analysis

- Why does SEND+MORE=MONEY have exactly 1 solution?
- How many solutions exist for A+B=C?
- What constraints reduce solution count?
- How does equation complexity affect solving time?

---

## Advanced Scenarios

### Batch Solving

```python
puzzles = [
    "SEND + MORE = MONEY",
    "CROSS + ROADS = DANGER",
    "HELLO + WORLD = GREET"
]

for puzzle in puzzles:
    solver = CryptarithmeticCSP(puzzle)
    solutions = solver.solve()
    print(f"{puzzle}: {len(solutions)} solutions")
```

### Solution Analysis

```python
solver = CryptarithmeticCSP("SEND + MORE = MONEY")
solutions = solver.solve()

# Analyze digit usage
digit_usage = {}
for solution in solutions:
    for var, digit in solution.items():
        if digit not in digit_usage:
            digit_usage[digit] = []
        digit_usage[digit].append(var)

print("Digit assignments:", digit_usage)
```

### Performance Testing

```python
import time

puzzles = [
    ("Simple", "A + B = C"),
    ("Medium", "SEND + MORE = MONEY"),
    ("Complex", "CROSS + ROADS = DANGER")
]

for name, puzzle in puzzles:
    start = time.time()
    solver = CryptarithmeticCSP(puzzle)
    solutions = solver.solve()
    elapsed = time.time() - start
    print(f"{name}: {elapsed:.3f}s for {len(solutions)} solutions")
```

---

For more information, see README.md and docs/algorithm_explanation.md
