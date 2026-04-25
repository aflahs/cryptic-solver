export type Mapping = Record<string, number>;

export interface SolutionDetails {
  mapping: Mapping;
  operand_values: Record<string, number>;
  result_value: number;
  equation: string;
  operand_strings: string[];
}

export class CryptarithmeticCSP {
  equation: string;
  original_equation: string;
  operands: string[] = [];
  result: string = '';
  operator: string = '';
  variables: string[] = [];
  leading_digits: Set<string> = new Set();
  solutions: Mapping[] = [];

  constructor(equation: string) {
    this.original_equation = equation;
    this.equation = equation.replace(/\s+/g, '');
    this._parseEquation();
  }

  private _parseEquation() {
    if (!this.equation.includes('=')) {
      throw new Error("Equation must contain '=' sign");
    }

    const [leftSide, resultSide] = this.equation.split('=');

    let operands: string[] = [];
    if (leftSide.includes('+')) {
      operands = leftSide.split('+');
      this.operator = '+';
    } else if (leftSide.includes('-')) {
      operands = leftSide.split('-');
      this.operator = '-';
    } else if (leftSide.includes('*')) {
      operands = leftSide.split('*');
      this.operator = '*';
    } else if (leftSide.includes('/')) {
      operands = leftSide.split('/');
      this.operator = '/';
    } else {
      throw new Error("Equation must contain an operator (+, -, *, /)");
    }

    this.operands = operands;
    this.result = resultSide;

    const allChars = this.equation.replace(/[-+*/=]/g, '').split('');
    this.variables = Array.from(new Set(allChars)).sort();

    for (const operand of this.operands) {
      if (operand.length > 1 && /[A-Za-z]/.test(operand[0])) {
        this.leading_digits.add(operand[0]);
      }
    }
    if (this.result.length > 1 && /[A-Za-z]/.test(this.result[0])) {
      this.leading_digits.add(this.result[0]);
    }

    if (this.variables.length > 10) {
      throw new Error("Too many unique letters (max 10)");
    }
  }

  private _isValidAssignment(assignment: Mapping): boolean {
    for (const leading of this.leading_digits) {
      if (assignment[leading] === 0) return false;
    }

    const getVal = (str: string) => {
      let val = 0;
      for (let i = 0; i < str.length; i++) {
        val = val * 10 + assignment[str[i]];
      }
      return val;
    };

    const operandValues = this.operands.map(getVal);
    const resultValue = getVal(this.result);

    if (this.operator === '+') {
      return operandValues.reduce((a, b) => a + b, 0) === resultValue;
    } else if (this.operator === '-') {
      return operandValues[0] - operandValues[1] === resultValue;
    } else if (this.operator === '*') {
      return operandValues.reduce((a, b) => a * b) === resultValue;
    } else if (this.operator === '/') {
      if (operandValues[1] === 0) return false;
      return Math.floor(operandValues[0] / operandValues[1]) === resultValue && (operandValues[0] % operandValues[1] === 0);
    }
    return false;
  }

  solve(): Mapping[] {
    this.solutions = [];
    const usedDigits = new Set<number>();
    const currentAssignment: Mapping = {};

    const backtrack = (varIndex: number) => {
      if (varIndex === this.variables.length) {
        if (this._isValidAssignment(currentAssignment)) {
          this.solutions.push({ ...currentAssignment });
        }
        return;
      }

      const currentVar = this.variables[varIndex];
      for (let digit = 0; digit <= 9; digit++) {
        // Fast fail for leading zero constraint
        if (digit === 0 && this.leading_digits.has(currentVar)) continue;
        
        if (!usedDigits.has(digit)) {
          usedDigits.add(digit);
          currentAssignment[currentVar] = digit;
          
          backtrack(varIndex + 1);
          
          usedDigits.delete(digit);
          delete currentAssignment[currentVar];
        }
      }
    };

    backtrack(0);
    return this.solutions;
  }

  getSolutionDetails(solution: Mapping): SolutionDetails {
    const operand_values: Record<string, number> = {};
    const operand_strings: string[] = [];

    const getVal = (str: string) => {
      let val = 0;
      for (let i = 0; i < str.length; i++) {
        val = val * 10 + solution[str[i]];
      }
      return val;
    };

    for (const operand of this.operands) {
      const val = getVal(operand);
      operand_values[operand] = val;
      operand_strings.push(`${operand} = ${val}`);
    }

    const result_value = getVal(this.result);
    const opValsArray = this.operands.map(op => operand_values[op]);

    let equation_result = '';
    if (this.operator === '+') {
      equation_result = `${opValsArray.join(' + ')} = ${result_value}`;
    } else if (this.operator === '-') {
      equation_result = `${opValsArray[0]} - ${opValsArray[1]} = ${result_value}`;
    } else if (this.operator === '*') {
      equation_result = `${opValsArray.join(' * ')} = ${result_value}`;
    } else if (this.operator === '/') {
      equation_result = `${opValsArray[0]} / ${opValsArray[1]} = ${result_value}`;
    }

    return {
      mapping: solution,
      operand_values,
      result_value,
      equation: equation_result,
      operand_strings
    };
  }
}
