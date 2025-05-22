import unittest
import io
import sys
from unittest.mock import patch

from src.capital_gains_cli import CapitalGainsCLI



class TestCapitalGainsCLI(unittest.TestCase):
    
    def setUp(self):
        self.cli = CapitalGainsCLI()
    
    def test_process_buy_and_sell_with_no_tax_due_to_small_operation(self):
        input_line = '[{"operation":"buy", "unit-cost":10.00, "quantity": 100},{"operation":"sell", "unit-cost":15.00, "quantity": 50},{"operation":"sell", "unit-cost":15.00, "quantity": 50}]'
        expected_output = '[{"tax": 0.0}, {"tax": 0.0}, {"tax": 0.0}]'
        
        result = self.cli.process_input(input_line)
        
        self.assertEqual(result, expected_output)
    
    def test_process_profit_and_loss_with_tax_on_profit(self):
        """Tests processing operations with profit (taxed) followed by loss (not taxed)."""
        input_line = '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":20.00, "quantity": 5000},{"operation":"sell", "unit-cost":5.00, "quantity": 5000}]'
        expected_output = '[{"tax": 0.0}, {"tax": 10000.0}, {"tax": 0.0}]'
        
        result = self.cli.process_input(input_line)
        
        self.assertEqual(result, expected_output)
    
    def test_process_loss_followed_by_profit_with_loss_deduction(self):
        input_line = '[{"operation":"buy", "unit-cost":10.00, "quantity": 10000},{"operation":"sell", "unit-cost":5.00, "quantity": 5000},{"operation":"sell", "unit-cost":20.00, "quantity": 3000}]'
        expected_output = '[{"tax": 0.0}, {"tax": 0.0}, {"tax": 1000.0}]'
        
        result = self.cli.process_input(input_line)
        
        self.assertEqual(result, expected_output)
    
    @patch('sys.stdin', io.StringIO('[{"operation":"buy", "unit-cost":10.00, "quantity": 100}]\n[{"operation":"sell", "unit-cost":20.00, "quantity": 50}]\n\n'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_with_multiple_independent_simulations(self, mock_stdout):
        self.cli.run()
        
        expected_output = '[{"tax": 0.0}]\n[{"tax": 0.0}]\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)
    
    @patch('sys.stdin', io.StringIO('invalid json\n\n'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_with_invalid_json_input_shows_error(self, mock_stdout):
        self.cli.run()
        
        expected_output = 'Error: Invalid JSON format\n'
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdin', io.BytesIO(b'{"operation":"buy", "unit-cost":10.00, "quantity": 100}\n'))
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_run_with_invalid_value(self, mock_stdout):
        self.cli.run()
        
        expected_output = "Error: string indices must be integers, not 'str'\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
