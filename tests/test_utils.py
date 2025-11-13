import pytest
from finpy.utils import apply_inflation


def test_apply_inflation():
    """Verify a value is correctly reduced by the inflation rate."""
    value = 1000.0
    inflation_rate = 0.02  # 2%
    adjusted_value = apply_inflation(value, inflation_rate)
    assert adjusted_value == pytest.approx(1000.0 / 1.02)
