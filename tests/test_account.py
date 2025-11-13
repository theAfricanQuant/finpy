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
