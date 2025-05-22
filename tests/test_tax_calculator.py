import unittest
from decimal import Decimal

from src.models.operation import Operation
from src.models.tax_result import TaxResult
from src.services.tax_calculator import TaxCalculator


class TestTaxCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calculator = TaxCalculator()
    
    def test_buy_and_sell_with_no_tax_due_to_small_operation_value(self):
        operations = [
            Operation("buy", 10.00, 100),
            Operation("sell", 15.00, 50),
            Operation("sell", 15.00, 50)
        ]
        
        expected = [
            TaxResult(Decimal('0')),
            TaxResult(Decimal('0')),
            TaxResult(Decimal('0'))
        ]
        
        results = self.calculator.calculate_taxes(operations)
        
        for i, (result, expected_result) in enumerate(zip(results, expected)):
            self.assertEqual(result.tax, expected_result.tax, f"Failed at item {i}")
    
    def test_profit_followed_by_loss_with_tax_on_profit(self):
        operations = [
            Operation("buy", 10.00, 10000),
            Operation("sell", 20.00, 5000),
            Operation("sell", 5.00, 5000)
        ]
        
        expected = [
            TaxResult(Decimal('0')),
            TaxResult(Decimal('10000')),
            TaxResult(Decimal('0'))
        ]
        
        results = self.calculator.calculate_taxes(operations)
        
        for i, (result, expected_result) in enumerate(zip(results, expected)):
            self.assertEqual(result.tax, expected_result.tax, f"Failed at item {i}")
    
    def test_loss_followed_by_profit_with_loss_deduction(self):
        operations = [
            Operation("buy", 10.00, 10000),
            Operation("sell", 5.00, 5000),
            Operation("sell", 20.00, 3000)
        ]
        
        expected = [
            TaxResult(Decimal('0')),
            TaxResult(Decimal('0')),
            TaxResult(Decimal('1000'))
        ]
        
        results = self.calculator.calculate_taxes(operations)
        
        for i, (result, expected_result) in enumerate(zip(results, expected)):
            self.assertEqual(result.tax, expected_result.tax, f"Failed at item {i}")
    
    def test_multiple_buys_with_weighted_average_and_no_profit(self):
        operations = [
            Operation("buy", 10.00, 10000),
            Operation("buy", 25.00, 5000),
            Operation("sell", 15.00, 10000)
        ]
        
        expected = [
            TaxResult(Decimal('0')),
            TaxResult(Decimal('0')),
            TaxResult(Decimal('0'))
        ]
        
        results = self.calculator.calculate_taxes(operations)
        
        for i, (result, expected_result) in enumerate(zip(results, expected)):
            self.assertEqual(result.tax, expected_result.tax, f"Failed at item {i}")
    
    def test_multiple_buys_and_sells_with_final_profit_and_tax(self):
        operations = [
            Operation("buy", 10.00, 10000),
            Operation("buy", 25.00, 5000),
            Operation("sell", 15.00, 10000),
            Operation("sell", 25.00, 5000)
        ]
        
        expected = [
            TaxResult(Decimal('0')),
            TaxResult(Decimal('0')),
            TaxResult(Decimal('0')),
            TaxResult(Decimal('10000'))
        ]
        
        results = self.calculator.calculate_taxes(operations)
        
        for i, (result, expected_result) in enumerate(zip(results, expected)):
            self.assertEqual(result.tax, expected_result.tax, f"Failed at item {i}")
    
    def test_weighted_average_calculation_with_multiple_buys(self):
        self.calculator._update_weighted_average(Decimal('10'), 10)
        self.assertEqual(self.calculator.weighted_average_price, Decimal('10'))
        
        self.calculator._update_weighted_average(Decimal('20'), 5)
        self.assertEqual(self.calculator.weighted_average_price, Decimal('13.33'))

    def test_profit_fully_offset_by_accumulated_loss(self):
        calculator = TaxCalculator()
        
        calculator._update_weighted_average(Decimal('10'), 5000)
        
        
        tax = calculator._calculate_sell_tax(Decimal('5'), 2000)
        
        self.assertEqual(tax, Decimal('0'))
        self.assertEqual(calculator.accumulated_loss, Decimal('10000'))
        
        tax = calculator._calculate_sell_tax(Decimal('15'), 1500)
        
        self.assertEqual(tax, Decimal('0'))
        self.assertEqual(calculator.accumulated_loss, Decimal('2500'))


if __name__ == "__main__":
    unittest.main()
