"""
Utility module for JSON processing and formatting.
"""

import json
from decimal import Decimal
from typing import List, Dict, Any

from src.models.operation import Operation
from src.models.tax_result import TaxResult


def parse_operations(json_str: str) -> List[Operation]:
    """
    Converts a JSON string into a list of operations.
    
    Args:
        json_str: JSON string containing the operations
        
    Returns:
        List of operations
        
    Raises:
        json.JSONDecodeError: If the string is not valid JSON
    """
    data = json.loads(json_str)
    return [Operation.from_dict(item) for item in data]


def format_results(results: List[TaxResult]) -> str:
    """
    Formats a list of tax results as a JSON string.
    
    Args:
        results: List of tax results
        
    Returns:
        JSON string representing the results
    """
    return json.dumps([result.to_dict() for result in results])


class DecimalEncoder(json.JSONEncoder):
    """
    Custom JSON encoder to handle Decimal objects.
    """
    def default(self, obj):
        if isinstance(obj, Decimal):
            return float(obj)
        return super(DecimalEncoder, self).default(obj)