import pytest
from finpy.taxes import (
    GERMAN_TAX_BRACKETS_2025,
    calculate_income_tax,
    calculate_capital_gains_tax,
)

def test_tax_brackets_structure():
    """Verify the data structure loads correctly and contains expected keys."""
    assert "single" in GERMAN_TAX_BRACKETS_2025
    assert "married" in GERMAN_TAX_BRACKETS_2025
    assert isinstance(GERMAN_TAX_BRACKETS_2025["single"], list)

def test_calculate_income_tax_single():
    """Test incomes in various brackets, at bracket boundaries, and zero income."""
    assert calculate_income_tax(0, "single") == 0.0
    assert calculate_income_tax(11604, "single") == 0.0
    assert calculate_income_tax(50000, "single") == pytest.approx((17005 - 11604) * 0.14 + (50000 - 17005) * 0.24)
    assert calculate_income_tax(100000, "single") == pytest.approx((17005 - 11604) * 0.14 + (66760 - 17005) * 0.24 + (100000 - 66760) * 0.42)

def test_calculate_income_tax_married():
    """Test incomes in various brackets for the joint status."""
    assert calculate_income_tax(0, "married") == 0.0
    assert calculate_income_tax(23208, "married") == 0.0
    assert calculate_income_tax(100000, "married") == pytest.approx((34010 - 23208) * 0.14 + (100000 - 34010) * 0.24)

def test_calculate_capital_gains_tax():
    """Verify the calculation with various capital gain amounts."""
    assert calculate_capital_gains_tax(1000) == 1000 * 0.26375
    assert calculate_capital_gains_tax(0) == 0.0
    assert calculate_capital_gains_tax(-100) == 0.0
