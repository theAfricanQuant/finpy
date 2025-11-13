from typing import Dict, List, Tuple

# FR2.3: Configurable tax laws for Germany 2025
GERMAN_TAX_BRACKETS_2025: Dict[str, List[Tuple[float, float]]] = {
    "single": [
        (11604, 0.0),
        (17005, 0.14),
        (66760, 0.24),
        (277825, 0.42),
        (float('inf'), 0.45),
    ],
    "married": [
        (23208, 0.0),
        (34010, 0.14),
        (133520, 0.24),
        (555650, 0.42),
        (float('inf'), 0.45),
    ]
}

# FR2.2: German Capital Gains Tax
GERMAN_CAPITAL_GAINS_TAX_RATE = 0.26375 # Abgeltungsteuer plus solidarity surcharge

def calculate_income_tax(income: float, status: str) -> float:
    """Calculates German income tax based on income and filing status."""
    if status not in GERMAN_TAX_BRACKETS_2025:
        raise ValueError("Invalid filing status")
    
    brackets = GERMAN_TAX_BRACKETS_2025[status]
    tax = 0.0
    last_bracket_limit = 0.0
    
    for limit, rate in brackets:
        if income > last_bracket_limit:
            taxable_in_bracket = min(income, limit) - last_bracket_limit
            tax += taxable_in_bracket * rate
            last_bracket_limit = limit
        else:
            break
            
    return tax

def calculate_capital_gains_tax(gains: float) -> float:
    """Calculates German capital gains tax."""
    if gains <= 0:
        return 0.0
    return gains * GERMAN_CAPITAL_GAINS_TAX_RATE
