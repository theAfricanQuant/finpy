def apply_inflation(value: float, rate: float) -> float:
    """Adjusts a monetary value for one period of inflation."""
    return value / (1 + rate)
