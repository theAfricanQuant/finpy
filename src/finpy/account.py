from dataclasses import dataclass
import random


@dataclass
class Account:
    """A base class for a financial account."""
    balance: float

    def deposit(self, amount: float) -> None:
        """Deposits a given amount into the account."""
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """Withdraws a given amount from the account."""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def project_growth(self, rate: float, std_dev: float = 0.0) -> None:
        """
        Projects the growth of the account balance over one period.
        Can be deterministic (std_dev=0) or stochastic.
        """
        if std_dev > 0:
            growth_rate = random.normalvariate(rate, std_dev)
        else:
            growth_rate = rate
        self.balance *= (1 + growth_rate)


class TaxableAccount(Account):
    """Represents a taxable brokerage account."""
    pass


class TaxDeferredAccount(Account):
    """Represents a tax-deferred account (e.g., Traditional IRA/401k)."""
    pass


class TaxExemptAccount(Account):
    """Represents a tax-exempt account (e.g., Roth IRA/401k)."""
    pass
