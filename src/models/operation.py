"""
Module that defines data models for financial operations.
"""

from decimal import Decimal
from enum import Enum
from typing import Dict, Any


class OperationType(Enum):
    """Enum representing the possible operation types."""
    BUY = "buy"
    SELL = "sell"


class Operation:
    """
    Class representing a financial operation for buying or selling stocks.
    """
    
    def __init__(self, operation_type: str, unit_cost: float, quantity: int):
        """
        Initializes a new operation.
        
        Args:
            operation_type: Type of operation ('buy' or 'sell')
            unit_cost: Unit price of the stock
            quantity: Number of stocks traded
        """
        self.operation_type = OperationType(operation_type)
        self.unit_cost = Decimal(str(unit_cost))
        self.quantity = quantity
    
    @property
    def total_value(self) -> Decimal:
        """Calculates the total value of the operation."""
        return self.unit_cost * self.quantity
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Operation':
        """
        Creates an Operation instance from a dictionary.
        
        Args:
            data: Dictionary containing the operation data
            
        Returns:
            A new Operation instance
        """
        return cls(
            operation_type=data["operation"],
            unit_cost=data["unit-cost"],
            quantity=data["quantity"]
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the operation to a dictionary.
        
        Returns:
            Dictionary representing the operation
        """
        return {
            "operation": self.operation_type.value,
            "unit-cost": float(self.unit_cost),
            "quantity": self.quantity
        }
