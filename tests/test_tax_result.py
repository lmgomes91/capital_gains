import unittest
from decimal import Decimal

from src.models.tax_result import TaxResult


class TestTaxResult(unittest.TestCase):
    """Tests for the TaxResult class."""
    
    def test_tax_result_initialization_stores_correct_value(self):
        """Tests that the initialization of a tax result stores the correct tax value."""
        tax_result = TaxResult(Decimal('10.50'))
        
        self.assertEqual(tax_result.tax, Decimal('10.50'))
    
    def test_to_dict_converts_tax_result_to_proper_dictionary(self):
        """Tests that to_dict method correctly converts a tax result to a dictionary with float value."""
        tax_result = TaxResult(Decimal('10.50'))
        
        expected = {"tax": 10.5}
        
        self.assertEqual(tax_result.to_dict(), expected)
    
    def test_to_dict_handles_zero_tax_correctly(self):
        """Tests that to_dict method correctly handles zero tax values."""
        tax_result = TaxResult(Decimal('0'))
        
        expected = {"tax": 0.0}
        
        self.assertEqual(tax_result.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
