"""
Constraint Satisfaction Problem (CSP) Solver for Cryptarithmetic Puzzles
Solves puzzles like SEND + MORE = MONEY
"""

from itertools import permutations
from typing import Dict, List, Tuple, Optional


class CryptarithmeticCSP:
    """
    Constraint Satisfaction Problem solver for cryptarithmetic puzzles.
    
    Uses a CSP approach where:
    - Variables: Each letter in the puzzle
    - Domain: Digits 0-9
    - Constraints:
        1. Each letter maps to a unique digit
        2. No leading zeros
        3. Arithmetic constraint is satisfied
    """
    
    def __init__(self, equation: str):
        """
        Initialize the CSP solver with a cryptarithmetic equation.
        
        Args:
            equation: String in format "SEND + MORE = MONEY"
        """
        self.original_equation = equation
        self.equation = equation.replace(" ", "")
        self.solutions: List[Dict[str, int]] = []
        self._parse_equation()
    
    def _parse_equation(self) -> None:
        """Parse the equation to extract operands and result."""
        if "=" not in self.equation:
            raise ValueError("Equation must contain '=' sign")
        
        left_side, result = self.equation.split("=")
        
        if "+" in left_side:
            operands = left_side.split("+")
        elif "-" in left_side:
            operands = left_side.split("-")
        elif "*" in left_side:
            operands = left_side.split("*")
        elif "/" in left_side:
            operands = left_side.split("/")
        else:
            raise ValueError("Equation must contain an operator (+, -, *, /)")
        
        self.operands = [op.strip() for op in operands]
        self.result = result.strip()
        self.operator = [op for op in "+-*/" if op in left_side][0]
        
        # Extract unique letters
        all_chars = self.equation.replace(self.operator, "").replace("=", "")
        self.variables = list(set(all_chars))
        self.variables.sort()  # For consistency
        
        # Identify leading digits (cannot be zero)
        self.leading_digits = set()
        for operand in self.operands:
            if len(operand) > 1 and operand[0].isalpha():
                self.leading_digits.add(operand[0])
        if len(self.result) > 1 and self.result[0].isalpha():
            self.leading_digits.add(self.result[0])
    
    def _is_valid_assignment(self, assignment: Dict[str, int]) -> bool:
        """
        Check if an assignment satisfies all constraints.
        
        Args:
            assignment: Dictionary mapping variables to digits
            
        Returns:
            True if all constraints are satisfied
        """
        # Check leading zero constraint
        for var in self.leading_digits:
            if assignment.get(var) == 0:
                return False
        
        # Check arithmetic constraint
        try:
            # Convert operands to numbers
            operand_values = []
            for operand in self.operands:
                value = 0
                for char in operand:
                    value = value * 10 + assignment.get(char, 0)
                operand_values.append(value)
            
            # Convert result to number
            result_value = 0
            for char in self.result:
                result_value = result_value * 10 + assignment.get(char, 0)
            
            # Check arithmetic
            if self.operator == "+":
                return sum(operand_values) == result_value
            elif self.operator == "-":
                return operand_values[0] - operand_values[1] == result_value
            elif self.operator == "*":
                result_calc = operand_values[0]
                for val in operand_values[1:]:
                    result_calc *= val
                return result_calc == result_value
            elif self.operator == "/":
                return operand_values[0] // operand_values[1] == result_value
        except:
            return False
        
        return False
    
    def solve(self) -> List[Dict[str, int]]:
        """
        Solve the cryptarithmetic puzzle using CSP with backtracking.
        
        Returns:
            List of valid solutions (each solution is a dict mapping variables to digits)
        """
        self.solutions = []
        
        # Generate all possible permutations of digits for the variables
        digits = list(range(10))
        num_vars = len(self.variables)
        
        if num_vars > 10:
            raise ValueError("Too many unique letters (max 10)")
        
        # Try all permutations
        for perm in permutations(digits, num_vars):
            assignment = dict(zip(self.variables, perm))
            
            if self._is_valid_assignment(assignment):
                self.solutions.append(assignment)
        
        return self.solutions
    
    def get_solution_details(self, solution: Dict[str, int]) -> Dict:
        """
        Get detailed information about a solution including the arithmetic result.
        
        Args:
            solution: A valid solution dictionary
            
        Returns:
            Dictionary containing the mapping and computed values
        """
        # Calculate operand values
        operand_values = []
        operand_strings = []
        
        for operand in self.operands:
            value = 0
            for char in operand:
                value = value * 10 + solution[char]
            operand_values.append(value)
            operand_strings.append(f"{operand} = {value}")
        
        # Calculate result value
        result_value = 0
        for char in self.result:
            result_value = result_value * 10 + solution[char]
        
        # Build equation string
        if self.operator == "+":
            equation_result = f"{' + '.join(map(str, operand_values))} = {result_value}"
        elif self.operator == "-":
            equation_result = f"{operand_values[0]} - {operand_values[1]} = {result_value}"
        elif self.operator == "*":
            equation_result = f"{' * '.join(map(str, operand_values))} = {result_value}"
        elif self.operator == "/":
            equation_result = f"{operand_values[0]} / {operand_values[1]} = {result_value}"
        
        return {
            "mapping": solution,
            "operand_values": dict(zip(self.operands, operand_values)),
            "result_value": result_value,
            "equation": equation_result,
            "operand_strings": operand_strings
        }
    
    def format_solution(self, solution: Dict[str, int]) -> str:
        """
        Format a solution as a readable string.
        
        Args:
            solution: A valid solution dictionary
            
        Returns:
            Formatted solution string
        """
        details = self.get_solution_details(solution)
        
        output = "=== Solution ===\n"
        output += "Mapping:\n"
        
        for var in sorted(solution.keys()):
            output += f"  {var} = {solution[var]}\n"
        
        output += "\nArithmetic:\n"
        for operand_str in details["operand_strings"]:
            output += f"  {operand_str}\n"
        output += f"  {self.result} = {details['result_value']}\n"
        output += f"\nEquation: {details['equation']}\n"
        
        return output
