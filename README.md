# Cryptarithmetic Solver Web Application

A Web Application designed to solve Cryptarithmetic Puzzles through robust Constraint Satisfaction Problem (CSP) algorithms.

---

## Problem Description

Cryptarithmetic is a genre of mathematical puzzles where digits (0-9) are replaced by letters of the alphabet. The objective is to decode the puzzle by finding the correct numeric value for each letter such that the mathematical equation holds true. 

The constraints that must be satisfied are:
1. Each letter must represent a unique digit. No two distinct letters can map to the same digit.
2. The arithmetic equation (Addition, Subtraction, Multiplication, or Division) must be mathematically correct.
3. Leading letters of any word or number block cannot represent the digit zero (e.g., in "SEND", the letter "S" cannot be 0).

---

## Algorithms Used

The solver leverages a **Backtracking Algorithm with Depth-First Search (DFS)** to efficiently traverse the state space of possible digit mappings. 

Instead of generating and evaluating all 3.6 million possible permutations of 10 digits naively, the backtracking approach assigns digits to variables one at a time. The algorithm implements **early pruning techniques**:
*   **Leading Zero Pruning:** If a variable represents the first letter of an operand, the algorithm instantly prunes branches attempting to assign the digit '0' to it.
*   **Constraint Checking:** Once a full mapping is constructed for a branch across the unique letters, the algorithm evaluates the arithmetic equation. If the sum holds true, the solution is recorded; otherwise, it backtracks and resumes the search.

This highly optimized client-side implementation yields computation times well under 100ms for standard puzzles.

---

## Execution Steps

To run the application on your local development environment, follow these steps:

1. **Install Dependencies**
   Navigate to the project directory in your terminal and install the required Node.js packages:
   ```bash
   npm install
   ```

2. **Start the Development Server**
   Launch the Next.js development server:
   ```bash
   npm run dev
   ```

3. **Access the Web Application**
   Open your preferred web browser and navigate to:
   ```text
   http://localhost:3000
   ```
   *You can interact with the solver by tying equations like "SEND + MORE = MONEY" into the Intelligence Core dashboard and clicking Compute.*

---

## Sample Outputs

**Input Equation:**
`SEND + MORE = MONEY`

**Variable Mappings:**
*   D = 7
*   E = 5
*   M = 1
*   N = 6
*   O = 0
*   R = 8
*   S = 9
*   Y = 2

**Arithmetic Verification:**
*   SEND = 9567
*   MORE = 1085
*   MONEY = 10652
*   **Equation:** 9567 + 1085 = 10652

---

## Team Details

*   **Team Member 1:** Muhammed Aflah S
*   **Registration Number:** RA2411026050147
