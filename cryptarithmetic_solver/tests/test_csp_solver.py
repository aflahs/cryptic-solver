"""
Unit tests for the Cryptarithmetic CSP Solver
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

import unittest
from csp_solver import CryptarithmeticCSP


class TestCryptarithmeticCSP(unittest.TestCase):
    """Test cases for CryptarithmeticCSP class."""
    
    def test_simple_addition(self):
        """Test a simple addition puzzle."""
        solver = CryptarithmeticCSP("A + B = C")
        solutions = solver.solve()
        
        # There should be multiple solutions for simple cases
        self.assertGreater(len(solutions), 0)
        
        # Verify first solution
        if solutions:
            solution = solutions[0]
            a = solution.get('A', 0)
            b = solution.get('B', 0)
            c = solution.get('C', 0)
            # A and B should not be zero (leading digits)
            self.assertNotEqual(a, 0)
            self.assertNotEqual(b, 0)
    
    def test_send_more_money(self):
        """Test the classic SEND + MORE = MONEY puzzle."""
        solver = CryptarithmeticCSP("SEND + MORE = MONEY")
        solutions = solver.solve()
        
        # There should be exactly one solution
        self.assertEqual(len(solutions), 1)
        
        # Verify the solution
        solution = solutions[0]
        expected = {'S': 9, 'E': 5, 'N': 6, 'D': 7, 'M': 1, 'O': 0, 'R': 8, 'Y': 2}
        self.assertEqual(solution, expected)
        
        # Verify arithmetic: 9567 + 1085 = 10652
        self.assertEqual(9567 + 1085, 10652)
    
    def test_solution_verification(self):
        """Test that solutions satisfy the arithmetic constraint."""
        solver = CryptarithmeticCSP("SEND + MORE = MONEY")
        solutions = solver.solve()
        
        for solution in solutions:
            details = solver.get_solution_details(solution)
            
            # Get operand values
            operand_vals = details['operand_values']
            operand_list = list(operand_vals.values())
            
            # Verify arithmetic
            result = sum(operand_list)
            self.assertEqual(result, details['result_value'])
    
    def test_unique_digits(self):
        """Test that all variables map to unique digits."""
        solver = CryptarithmeticCSP("SEND + MORE = MONEY")
        solutions = solver.solve()
        
        for solution in solutions:
            # Get all digit values
            digits = list(solution.values())
            # Check uniqueness
            self.assertEqual(len(digits), len(set(digits)))
    
    def test_no_leading_zeros(self):
        """Test that leading digits are not zero."""
        solver = CryptarithmeticCSP("SEND + MORE = MONEY")
        solutions = solver.solve()
        
        for solution in solutions:
            # Check leading digits
            for var in solver.leading_digits:
                self.assertNotEqual(solution[var], 0, f"{var} should not be 0")
    
    def test_parse_equation_addition(self):
        """Test equation parsing for addition."""
        solver = CryptarithmeticCSP("ABC + DEF = GHI")
        
        self.assertEqual(solver.operator, "+")
        self.assertEqual(solver.operands, ["ABC", "DEF"])
        self.assertEqual(solver.result, "GHI")
        self.assertEqual(len(solver.variables), 9)
    
    def test_parse_equation_subtraction(self):
        """Test equation parsing for subtraction."""
        solver = CryptarithmeticCSP("ABC - DEF = GHI")
        
        self.assertEqual(solver.operator, "-")
        self.assertEqual(solver.operands, ["ABC", "DEF"])
        self.assertEqual(solver.result, "GHI")
    
    def test_invalid_equation(self):
        """Test handling of invalid equations."""
        with self.assertRaises(ValueError):
            CryptarithmeticCSP("INVALID")
    
    def test_whitespace_handling(self):
        """Test that equations with extra whitespace are handled correctly."""
        solver1 = CryptarithmeticCSP("SEND + MORE = MONEY")
        solver2 = CryptarithmeticCSP("  SEND  +  MORE  =  MONEY  ")
        
        solutions1 = solver1.solve()
        solutions2 = solver2.solve()
        
        self.assertEqual(len(solutions1), len(solutions2))
    
    def test_solution_details(self):
        """Test that solution details are formatted correctly."""
        solver = CryptarithmeticCSP("SEND + MORE = MONEY")
        solutions = solver.solve()
        
        if solutions:
            solution = solutions[0]
            details = solver.get_solution_details(solution)
            
            # Check keys in details
            self.assertIn('mapping', details)
            self.assertIn('operand_values', details)
            self.assertIn('result_value', details)
            self.assertIn('equation', details)
            self.assertIn('operand_strings', details)
            
            # Verify mapping matches solution
            self.assertEqual(details['mapping'], solution)
    
    def test_cross_roads_danger(self):
        """Test the CROSS + ROADS = DANGER puzzle."""
        solver = CryptarithmeticCSP("CROSS + ROADS = DANGER")
        solutions = solver.solve()
        
        # Should have at least one solution
        self.assertGreater(len(solutions), 0)
        
        # Verify all solutions
        for solution in solutions:
            # Extract values
            cross = int(''.join(str(solution[c]) for c in 'CROSS'))
            roads = int(''.join(str(solution[c]) for c in 'ROADS'))
            danger = int(''.join(str(solution[c]) for c in 'DANGER'))
            
            # Verify arithmetic
            self.assertEqual(cross + roads, danger)
    
    def test_format_solution(self):
        """Test that solution formatting works."""
        solver = CryptarithmeticCSP("SEND + MORE = MONEY")
        solutions = solver.solve()
        
        if solutions:
            solution = solutions[0]
            formatted = solver.format_solution(solution)
            
            # Check that formatted output contains expected elements
            self.assertIn("Solution", formatted)
            self.assertIn("Mapping", formatted)
            self.assertIn("Arithmetic", formatted)
            self.assertIn("=", formatted)


class TestMultipleOperands(unittest.TestCase):
    """Test cases with multiple operands."""
    
    def test_three_operands_addition(self):
        """Test addition with three operands."""
        solver = CryptarithmeticCSP("A + B + C = D")
        solutions = solver.solve()
        
        # Should have solutions
        self.assertGreater(len(solutions), 0)
        
        # Verify a solution
        if solutions:
            solution = solutions[0]
            a = solution['A']
            b = solution['B']
            c = solution['C']
            d = solution['D']
            
            # Verify arithmetic
            self.assertEqual(a + b + c, d)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""
    
    def test_single_digit_variables(self):
        """Test puzzle with single digit variables."""
        solver = CryptarithmeticCSP("A + A = B")
        solutions = solver.solve()
        
        # Should have solutions
        self.assertGreater(len(solutions), 0)
    
    def test_solution_with_zeros(self):
        """Test that zero can be used in non-leading positions."""
        solver = CryptarithmeticCSP("AB + CD = EF")
        solutions = solver.solve()
        
        # All variables are leading digits, so zero won't be used
        # But let's test a case where zero CAN be used
        # For SEND + MORE = MONEY, O = 0
        solver2 = CryptarithmeticCSP("SEND + MORE = MONEY")
        solutions2 = solver2.solve()
        
        # At least one solution should use zero in a non-leading position
        has_zero = False
        for solution in solutions2:
            if 0 in solution.values():
                has_zero = True
                break
        
        self.assertTrue(has_zero)


if __name__ == '__main__':
    unittest.main()
