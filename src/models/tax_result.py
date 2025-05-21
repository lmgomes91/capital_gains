"""
Module that defines the tax calculation result.
"""

from decimal import Decimal
from typing import Dict, Any


class TaxResult:
    """
    Class representing the tax calculation result for an operation.
    """
    
    def __init__(self, tax: Decimal):
        """
        Initializes a new tax result.
        
        Args:
            tax: Calculated tax amount
        """
        self.tax = tax
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the result to a dictionary.
        
        Returns:
            Dictionary representing the tax result
        """
        return {"tax": float(self.tax)}
