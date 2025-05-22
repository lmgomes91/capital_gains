"""
Main module that implements the command line interface for tax calculation.
"""

import sys
import json

from src.services.tax_calculator import TaxCalculator
from src.utils.json_utils import parse_operations, format_results


class CapitalGainsCLI:
    """
    Class that implements the command line interface for tax calculation.
    """
    
    def __init__(self):
        """Initializes the command line interface."""
        self.calculator = TaxCalculator()
    
    def process_input(self, input_line: str) -> str:
        """
        Processes an input line and returns the result as a JSON string.
        
        Args:
            input_line: Input line in JSON format
            
        Returns:
            Result of the processing in JSON format
            
        Raises:
            json.JSONDecodeError: If the input is not valid JSON
        """
        operations = parse_operations(input_line)
        results = self.calculator.calculate_taxes(operations)
        return format_results(results)
    
    def run(self):
        """
        Executes the command line input/output processing.
        Reads from standard input and writes to standard output.
        """
        for line in sys.stdin:
            line = line.strip()
            if not line:
                break
            
            try:
                result = self.process_input(line)
                print(result)
            except json.JSONDecodeError:
                print("Error: Invalid JSON format")
            except Exception as e:
                print(f"Error: {str(e)}")
