from dataclasses import dataclass
from typing import Dict, Any
import pandas as pd
import copy

from .account import TaxableAccount, TaxDeferredAccount, TaxExemptAccount
from .taxes import calculate_income_tax, calculate_capital_gains_tax

@dataclass
class SimulationConfig:
    """Holds all user inputs for a retirement simulation."""
    current_age: int
    retirement_age: int
    end_age: int
    annual_contribution: float
    retirement_expenses: float
    investment_return: float
    investment_std_dev: float
    inflation_rate: float
    filing_status: str


class Portfolio:
    """Holds and manages the different account types."""
    def __init__(self, taxable: TaxableAccount, tax_deferred: TaxDeferredAccount, tax_exempt: TaxExemptAccount):
        self.taxable = taxable
        self.tax_deferred = tax_deferred
        self.tax_exempt = tax_exempt

    @property
    def total_balance(self) -> float:
        """Returns the total balance across all accounts."""
        return self.taxable.balance + self.tax_deferred.balance + self.tax_exempt.balance


class RetirementSimulator:
    """Runs retirement projection simulations."""
    def __init__(self, portfolio: Portfolio, config: SimulationConfig):
        self._initial_portfolio = copy.deepcopy(portfolio)
        self._initial_config = copy.deepcopy(config)
        self.portfolio = portfolio
        self.config = config

    def _reset_state(self):
        """Resets the simulator to its initial state."""
        self.portfolio = copy.deepcopy(self._initial_portfolio)
        self.config = copy.deepcopy(self._initial_config)

    def _run_single_year(self, current_age: int, expenses: float):
        # Contributions (pre-retirement)
        if current_age < self.config.retirement_age:
            self.portfolio.tax_deferred.deposit(self.config.annual_contribution)

        # Growth
        for acc in [self.portfolio.taxable, self.portfolio.tax_deferred, self.portfolio.tax_exempt]:
            acc.project_growth(self.config.investment_return, self.config.investment_std_dev)

        # Withdrawals (post-retirement)
        if current_age >= self.config.retirement_age:
            needed = expenses
            
            # Taxable
            withdrawn_taxable = min(needed, self.portfolio.taxable.balance)
            if withdrawn_taxable > 0:
                self.portfolio.taxable.withdraw(withdrawn_taxable)
                needed -= withdrawn_taxable
                capital_gains_tax = calculate_capital_gains_tax(withdrawn_taxable)
                self.portfolio.taxable.withdraw(capital_gains_tax)

            # Tax-deferred
            if needed > 0 and self.portfolio.tax_deferred.balance > 0:
                withdrawn_deferred = min(needed, self.portfolio.tax_deferred.balance)
                self.portfolio.tax_deferred.withdraw(withdrawn_deferred)
                needed -= withdrawn_deferred
                income_tax = calculate_income_tax(withdrawn_deferred, self.config.filing_status)
                self.portfolio.taxable.withdraw(income_tax)
            
            # Tax-exempt
            if needed > 0 and self.portfolio.tax_exempt.balance > 0:
                withdrawn_exempt = min(needed, self.portfolio.tax_exempt.balance)
                self.portfolio.tax_exempt.withdraw(withdrawn_exempt)

    def run_deterministic_simulation(self) -> pd.DataFrame:
        """Runs a single simulation with deterministic returns."""
        self._reset_state()
        self.config.investment_std_dev = 0.0

        results = []
        current_expenses = self.config.retirement_expenses
        
        for age in range(self.config.current_age, self.config.end_age + 1):
            if self.portfolio.total_balance < 0:
                self.portfolio.taxable.balance = 0
                self.portfolio.tax_deferred.balance = 0
                self.portfolio.tax_exempt.balance = 0
            
            self._run_single_year(age, current_expenses)
            results.append({
                "Age": age,
                "Taxable": self.portfolio.taxable.balance,
                "Tax-Deferred": self.portfolio.tax_deferred.balance,
                "Tax-Exempt": self.portfolio.tax_exempt.balance,
                "Total": self.portfolio.total_balance,
            })
            current_expenses *= (1 + self.config.inflation_rate)

        self._reset_state() # Restore original config and portfolio
        return pd.DataFrame(results)

    def run_monte_carlo_simulation(self, iterations: int) -> Dict[str, Any]:
        """Runs multiple simulations with stochastic returns."""
        final_balances = []
        
        for _ in range(iterations):
            self._reset_state()
            current_expenses = self.config.retirement_expenses
            
            for age in range(self.config.current_age, self.config.end_age + 1):
                if self.portfolio.total_balance <= 0:
                    break
                self._run_single_year(age, current_expenses)
                current_expenses *= (1 + self.config.inflation_rate)
            
            final_balances.append(self.portfolio.total_balance)

        self._reset_state()

        successful_retirements = sum(1 for b in final_balances if b > 0)
        success_rate = successful_retirements / iterations if iterations > 0 else 0.0
        
        return {
            "success_rate": success_rate,
            "final_balances": final_balances
        }
