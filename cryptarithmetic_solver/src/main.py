"""
Main entry point for Cryptarithmetic Puzzle Solver
Supports both GUI and CLI modes
"""

import sys
import argparse
from csp_solver import CryptarithmeticCSP


def solve_cli(equation: str, verbose: bool = True):
    """
    Solve a cryptarithmetic puzzle using CLI.
    
    Args:
        equation: The puzzle equation as a string
        verbose: Whether to print detailed output
    """
    try:
        solver = CryptarithmeticCSP(equation)
        solutions = solver.solve()
        
        if verbose:
            print(f"\nPuzzle: {equation}")
            print(f"Unique letters: {', '.join(sorted(solver.variables))}")
            print(f"Number of solutions: {len(solutions)}\n")
        
        if not solutions:
            print("No solutions found for this puzzle.")
            return False
        
        for i, solution in enumerate(solutions, 1):
            print(f"\n{solver.format_solution(solution)}")
        
        return True
    
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Cryptarithmetic Puzzle Solver using Constraint Satisfaction Problem (CSP) approach",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --gui                           # Launch GUI application
  python main.py "SEND + MORE = MONEY"           # Solve from command line
  python main.py "CROSS + ROADS = DANGER"        # Another example
  python main.py "A + B = C"                     # Simple example
        """
    )
    
    parser.add_argument(
        "equation",
        nargs="?",
        help="Cryptarithmetic equation (e.g., 'SEND + MORE = MONEY')"
    )
    
    parser.add_argument(
        "--gui",
        action="store_true",
        help="Launch the GUI application"
    )
    
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        default=True,
        help="Verbose output (default: True)"
    )
    
    args = parser.parse_args()
    
    # If --gui flag is set, launch GUI
    if args.gui or (not args.equation):
        try:
            from gui import main as gui_main
            gui_main()
        except ImportError:
            print("Error: tkinter is required for GUI mode")
            print("Please install tkinter or use CLI mode with an equation argument")
            sys.exit(1)
    else:
        # CLI mode
        success = solve_cli(args.equation, args.verbose)
        sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
