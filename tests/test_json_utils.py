import unittest
import json
from decimal import Decimal

from src.models.tax_result import TaxResult
from src.utils.json_utils import parse_operations, format_results, DecimalEncoder


class TestJsonUtils(unittest.TestCase):
    
    def test_parse_operations(self):
        json_str = '[{"operation":"buy", "unit-cost":10.00, "quantity": 100},{"operation":"sell", "unit-cost":15.00, "quantity": 50}]'
        
        operations = parse_operations(json_str)
        
        self.assertEqual(len(operations), 2)
        self.assertEqual(operations[0].operation_type.value, "buy")
        self.assertEqual(operations[0].unit_cost, Decimal('10.00'))
        self.assertEqual(operations[0].quantity, 100)
        self.assertEqual(operations[1].operation_type.value, "sell")
        self.assertEqual(operations[1].unit_cost, Decimal('15.00'))
        self.assertEqual(operations[1].quantity, 50)
    
    def test_format_results(self):
        results = [
            TaxResult(Decimal('0')),
            TaxResult(Decimal('10000.50'))
        ]
        
        json_str = format_results(results)
        data = json.loads(json_str)
        
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]["tax"], 0.0)
        self.assertEqual(data[1]["tax"], 10000.5)
    
    def test_decimal_encoder(self):
        data = {
            "value": Decimal('123.45')
        }
        
        json_str = json.dumps(data, cls=DecimalEncoder)
        parsed_data = json.loads(json_str)
        
        self.assertEqual(parsed_data["value"], 123.45)

    def test_decimal_encoder_raises_type_error(self):
        self.assertRaises(TypeError, json.dumps, b'123', cls=DecimalEncoder)
       


if __name__ == "__main__":
    unittest.main()
