import pytest
from finpy.account import Account, TaxableAccount, TaxDeferredAccount, TaxExemptAccount


def test_account_initialization():
    """Verify an account can be created with an initial balance."""
    initial_balance = 1000.0
    account = Account(balance=initial_balance)
    assert account.balance == initial_balance


def test_account_subclass_creation():
    """Verify instances of each subclass can be created correctly."""
    taxable_acc = TaxableAccount(balance=100.0)
    tax_deferred_acc = TaxDeferredAccount(balance=200.0)
    tax_exempt_acc = TaxExemptAccount(balance=300.0)

    assert isinstance(taxable_acc, Account)
    assert isinstance(tax_deferred_acc, Account)
    assert isinstance(tax_exempt_acc, Account)

    assert taxable_acc.balance == 100.0
    assert tax_deferred_acc.balance == 200.0
    assert tax_exempt_acc.balance == 300.0


def test_deposit_increases_balance():
    """Verify that depositing funds increases the account balance."""
    account = Account(balance=1000.0)
    account.deposit(500.0)
    assert account.balance == 1500.0


def test_withdraw_decreases_balance():
    """Verify that withdrawing funds decreases the account balance."""
    account = Account(balance=1000.0)
    account.withdraw(200.0)
    assert account.balance == 800.0


def test_withdraw_raises_error_on_insufficient_funds():
    """Verify withdrawing more than the balance raises a ValueError."""
    account = Account(balance=100.0)
    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(200.0)


def test_project_growth_increases_balance():
    """Verify balance is correctly increased by the return rate."""
    account = Account(balance=1000.0)
    account.project_growth(0.10)  # 10% growth
    assert account.balance == 1100.0
