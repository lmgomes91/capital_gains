
"""
Module that implements the tax calculation logic for capital gains.
"""

from decimal import Decimal, ROUND_HALF_UP
from typing import List

from src.models.operation import Operation, OperationType
from src.models.tax_result import TaxResult


class TaxCalculator:
    """
    Class responsible for calculating taxes on financial operations.
    """
    
    def __init__(self):
        """Initializes the tax calculator with zeroed state."""
        self.reset_state()
    
    def reset_state(self):
        """Resets the state for a new simulation."""
        self.weighted_average_price = Decimal('0')
        self.total_shares = 0
        self.accumulated_loss = Decimal('0')
    
    def calculate_taxes(self, operations: List[Operation]) -> List[TaxResult]:
        """
        Calculates the tax for a list of operations.
        
        Args:
            operations: List of operations to be processed
            
        Returns:
            List of tax results for each operation
        """
        self.reset_state()
        results = []
        
        for operation in operations:
            if operation.operation_type == OperationType.BUY:
                # Buy operations don't pay taxes
                self._update_weighted_average(operation.unit_cost, operation.quantity)
                results.append(TaxResult(Decimal('0')))
            elif operation.operation_type == OperationType.SELL:
                # Calculate tax for sell operations
                tax = self._calculate_sell_tax(operation.unit_cost, operation.quantity)
                results.append(TaxResult(tax))
        
        return results
    
    def _update_weighted_average(self, unit_cost: Decimal, quantity: int):
        """
        Updates the weighted average price when buying stocks.
        
        Args:
            unit_cost: Unit price of the stock
            quantity: Number of stocks purchased
        """
        if self.total_shares == 0:
            self.weighted_average_price = unit_cost
            self.total_shares = quantity
        else:
            total_value = (self.weighted_average_price * self.total_shares) + (unit_cost * quantity)
            self.total_shares += quantity
            self.weighted_average_price = (total_value / self.total_shares).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    
    def _calculate_sell_tax(self, unit_cost: Decimal, quantity: int) -> Decimal:
        """
        Calculates the tax to be paid in a sell operation.
        
        Args:
            unit_cost: Unit price of the stock
            quantity: Number of stocks sold
            
        Returns:
            Tax amount to be paid
        """
        # Update total shares after the sale
        self.total_shares -= quantity
        
        # Calculate profit or loss
        operation_value = unit_cost * quantity
        cost_basis = self.weighted_average_price * quantity
        profit_or_loss = operation_value - cost_basis
        
        # If it's a loss, accumulate to deduct from future profits
        if profit_or_loss < 0:
            self.accumulated_loss += abs(profit_or_loss)
            return Decimal('0')
        
        # If the total value of the operation is less than or equal to R$ 20,000.00, no tax is paid
        if operation_value <= Decimal('20000'):
            return Decimal('0')
        
        # Deduct accumulated losses from current profit
        if self.accumulated_loss > 0:
            if profit_or_loss <= self.accumulated_loss:
                self.accumulated_loss -= profit_or_loss
                return Decimal('0')
            else:
                taxable_profit = profit_or_loss - self.accumulated_loss
                self.accumulated_loss = Decimal('0')
                # Calculate 20% tax on taxable profit
                return (taxable_profit * Decimal('0.2')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        
        # Calculate 20% tax on profit
        return (profit_or_loss * Decimal('0.2')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
