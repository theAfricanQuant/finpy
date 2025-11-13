from dataclasses import dataclass


@dataclass
class Account:
    """A base class for a financial account."""
    balance: float


class TaxableAccount(Account):
    """Represents a taxable brokerage account."""
    pass


class TaxDeferredAccount(Account):
    """Represents a tax-deferred account (e.g., Traditional IRA/401k)."""
    pass


class TaxExemptAccount(Account):
    """Represents a tax-exempt account (e.g., Roth IRA/401k)."""
    pass
