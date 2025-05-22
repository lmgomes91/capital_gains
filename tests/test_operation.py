import unittest
from decimal import Decimal

from src.models.operation import Operation, OperationType


class TestOperation(unittest.TestCase):
    
    def test_operation_initialization(self):
        operation = Operation("buy", 10.00, 100)
        
        self.assertEqual(operation.operation_type, OperationType.BUY)
        self.assertEqual(operation.unit_cost, Decimal('10.00'))
        self.assertEqual(operation.quantity, 100)
    
    def test_total_value_calculation(self):
        operation = Operation("sell", 15.50, 50)
        
        self.assertEqual(operation.total_value, Decimal('775.00'))
    
    def test_from_dict(self):
        data = {
            "operation": "buy",
            "unit-cost": 10.00,
            "quantity": 100
        }
        
        operation = Operation.from_dict(data)
        
        self.assertEqual(operation.operation_type, OperationType.BUY)
        self.assertEqual(operation.unit_cost, Decimal('10.00'))
        self.assertEqual(operation.quantity, 100)
    
    def test_to_dict(self):
        operation = Operation("sell", 15.50, 50)
        
        expected = {
            "operation": "sell",
            "unit-cost": 15.5,
            "quantity": 50
        }
        
        self.assertEqual(operation.to_dict(), expected)


if __name__ == "__main__":
    unittest.main()
