"""
GUI Interface for Cryptarithmetic Puzzle Solver
Uses tkinter for cross-platform compatibility
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
from csp_solver import CryptarithmeticCSP


class CryptarithmeticGUI:
    """GUI Application for solving cryptarithmetic puzzles."""
    
    def __init__(self, root):
        """Initialize the GUI application."""
        self.root = root
        self.root.title("Cryptarithmetic Puzzle Solver")
        self.root.geometry("900x750")
        self.root.resizable(True, True)
        
        # Configure style
        self.root.configure(bg="#f0f0f0")
        
        self.solver = None
        self.current_solutions = []
        self.current_solution_index = 0
        
        self._create_widgets()
        self._load_examples()
    
    def _create_widgets(self):
        """Create GUI widgets."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title = ttk.Label(
            main_frame,
            text="Cryptarithmetic Puzzle Solver (CSP Approach)",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=10)
        
        # Input section
        input_frame = ttk.LabelFrame(main_frame, text="Puzzle Input", padding="10")
        input_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(input_frame, text="Enter equation (e.g., SEND + MORE = MONEY):").pack(anchor=tk.W)
        
        self.equation_var = tk.StringVar(value="SEND + MORE = MONEY")
        self.equation_entry = ttk.Entry(input_frame, textvariable=self.equation_var, width=50, font=("Arial", 11))
        self.equation_entry.pack(fill=tk.X, pady=5)
        
        # Example button
        ttk.Label(input_frame, text="Quick examples:").pack(anchor=tk.W, pady=(10, 5))
        
        examples_frame = ttk.Frame(input_frame)
        examples_frame.pack(fill=tk.X, pady=5)
        
        self.example_var = tk.StringVar(value="SEND + MORE = MONEY")
        
        examples = [
            ("SEND + MORE = MONEY", "SEND + MORE = MONEY"),
            ("CROSS + ROADS = DANGER", "CROSS + ROADS = DANGER"),
            ("HELLO + WORLD = GREET", "HELLO + WORLD = GREET"),
            ("TWELVE + TWELVE = TWENTY", "TWELVE + TWELVE = TWENTY"),
        ]
        
        for label, value in examples:
            ttk.Button(
                examples_frame,
                text=label,
                command=lambda v=value: self._load_example(v)
            ).pack(side=tk.LEFT, padx=2)
        
        # Buttons
        button_frame = ttk.Frame(input_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        self.solve_btn = ttk.Button(button_frame, text="Solve Puzzle", command=self._solve_puzzle)
        self.solve_btn.pack(side=tk.LEFT, padx=5)
        
        self.clear_btn = ttk.Button(button_frame, text="Clear", command=self._clear)
        self.clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Status label
        self.status_var = tk.StringVar(value="Ready")
        status_label = ttk.Label(input_frame, textvariable=self.status_var, foreground="blue")
        status_label.pack(anchor=tk.W, pady=5)
        
        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Solutions", padding="10")
        results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Solution counter
        self.counter_var = tk.StringVar(value="No solutions yet")
        counter_label = ttk.Label(results_frame, textvariable=self.counter_var, font=("Arial", 10, "bold"))
        counter_label.pack(anchor=tk.W, pady=5)
        
        # Results text area
        self.results_text = scrolledtext.ScrolledText(
            results_frame,
            height=20,
            width=100,
            font=("Courier", 10),
            bg="white",
            fg="black"
        )
        self.results_text.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Configure text tags for colored output
        self.results_text.tag_configure("header", foreground="#1f77b4", font=("Courier", 10, "bold"))
        self.results_text.tag_configure("mapping", foreground="#2ca02c", font=("Courier", 10))
        self.results_text.tag_configure("equation", foreground="#d62728", font=("Courier", 10, "bold"))
        self.results_text.tag_configure("success", foreground="#27ae60", font=("Courier", 10, "bold"))
        
        # Navigation buttons
        nav_frame = ttk.Frame(results_frame)
        nav_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(nav_frame, text="< Previous", command=self._show_previous).pack(side=tk.LEFT, padx=5)
        ttk.Button(nav_frame, text="Next >", command=self._show_next).pack(side=tk.LEFT, padx=5)
        
        # Information section
        info_frame = ttk.LabelFrame(main_frame, text="Information", padding="10")
        info_frame.pack(fill=tk.X, pady=10)
        
        info_text = """
Cryptarithmetic Puzzle: A mathematical puzzle where letters represent unique digits (0-9).
Algorithm: Constraint Satisfaction Problem (CSP) with backtracking and permutation-based search.
Constraints:
  1. Each letter must map to a unique digit (0-9)
  2. No leading zeros allowed for multi-digit numbers
  3. The arithmetic equation must be satisfied
        """
        
        info_label = ttk.Label(info_frame, text=info_text.strip(), justify=tk.LEFT)
        info_label.pack(anchor=tk.W)
    
    def _load_examples(self):
        """Load example puzzles."""
        self.examples = {
            "SEND + MORE = MONEY": "SEND + MORE = MONEY",
            "CROSS + ROADS = DANGER": "CROSS + ROADS = DANGER",
        }
    
    def _load_example(self, equation):
        """Load an example puzzle."""
        self.equation_var.set(equation)
    
    def _solve_puzzle(self):
        """Solve the puzzle in a separate thread."""
        equation = self.equation_var.get().strip()
        
        if not equation:
            messagebox.showerror("Error", "Please enter a puzzle equation!")
            return
        
        # Disable solve button during solving
        self.solve_btn.config(state=tk.DISABLED)
        self.status_var.set("Solving... Please wait")
        self.root.update()
        
        # Run solver in separate thread to keep GUI responsive
        thread = threading.Thread(target=self._solve_thread, args=(equation,))
        thread.daemon = True
        thread.start()
    
    def _solve_thread(self, equation):
        """Thread function to solve the puzzle."""
        try:
            self.solver = CryptarithmeticCSP(equation)
            self.current_solutions = self.solver.solve()
            self.current_solution_index = 0
            
            # Update GUI
            self.root.after(0, self._display_solutions)
            
        except ValueError as e:
            self.root.after(0, lambda: messagebox.showerror("Error", str(e)))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Error", f"An error occurred: {str(e)}"))
        finally:
            self.root.after(0, self._enable_buttons)
    
    def _display_solutions(self):
        """Display the solutions found."""
        if not self.current_solutions:
            self.results_text.config(state=tk.NORMAL)
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, "No solutions found for this puzzle!", "equation")
            self.results_text.config(state=tk.DISABLED)
            self.counter_var.set("No solutions found")
            self.status_var.set("No solutions exist for this puzzle")
            return
        
        self.counter_var.set(
            f"Solution {self.current_solution_index + 1} of {len(self.current_solutions)}"
        )
        self.status_var.set(f"Found {len(self.current_solutions)} solution(s)!")
        self._show_solution(self.current_solution_index)
    
    def _show_solution(self, index):
        """Display a specific solution."""
        if not self.current_solutions or index < 0 or index >= len(self.current_solutions):
            return
        
        solution = self.current_solutions[index]
        details = self.solver.get_solution_details(solution)
        
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        
        # Display original equation
        self.results_text.insert(tk.END, "Original Puzzle:\n", "header")
        self.results_text.insert(tk.END, f"  {self.solver.original_equation}\n\n")
        
        # Display mapping
        self.results_text.insert(tk.END, "Variable Mapping:\n", "header")
        for var in sorted(solution.keys()):
            self.results_text.insert(tk.END, f"  {var} → {solution[var]}\n", "mapping")
        
        # Display arithmetic
        self.results_text.insert(tk.END, "\nArithmetic Verification:\n", "header")
        for operand_str in details["operand_strings"]:
            self.results_text.insert(tk.END, f"  {operand_str}\n", "mapping")
        self.results_text.insert(tk.END, f"  {self.solver.result} → {details['result_value']}\n", "mapping")
        
        # Display final equation
        self.results_text.insert(tk.END, "\nFinal Equation:\n", "header")
        self.results_text.insert(tk.END, f"  {details['equation']}\n", "success")
        
        self.results_text.config(state=tk.DISABLED)
        self.counter_var.set(
            f"Solution {self.current_solution_index + 1} of {len(self.current_solutions)}"
        )
    
    def _show_previous(self):
        """Show the previous solution."""
        if self.current_solutions:
            self.current_solution_index = (self.current_solution_index - 1) % len(self.current_solutions)
            self._show_solution(self.current_solution_index)
    
    def _show_next(self):
        """Show the next solution."""
        if self.current_solutions:
            self.current_solution_index = (self.current_solution_index + 1) % len(self.current_solutions)
            self._show_solution(self.current_solution_index)
    
    def _clear(self):
        """Clear the interface."""
        self.equation_var.set("")
        self.results_text.config(state=tk.NORMAL)
        self.results_text.delete(1.0, tk.END)
        self.results_text.config(state=tk.DISABLED)
        self.counter_var.set("No solutions yet")
        self.status_var.set("Ready")
        self.current_solutions = []
        self.current_solution_index = 0
    
    def _enable_buttons(self):
        """Re-enable buttons after solving."""
        self.solve_btn.config(state=tk.NORMAL)


def main():
    """Main entry point for the GUI application."""
    root = tk.Tk()
    app = CryptarithmeticGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
