# 🚀 FinPy

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.14-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://github.com/astral-sh/ruff)
[![Tests](https://img.shields.io/badge/tests-pytest-orange.svg)](https://pytest.org)

**A modern Python library for financial analysis and quantitative finance**

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Contributing](#-contributing)

</div>

---

## 📊 Overview

**FinPy** is a sophisticated retirement planning and financial simulation library designed for the German market. Built with precision and ease-of-use in mind, FinPy enables individuals, financial advisors, and analysts to model retirement scenarios with accurate German tax calculations and Monte Carlo simulations.

### ✨ Key Highlights

- 🇩🇪 **German Tax Compliant** - Accurate 2025 German tax brackets and capital gains calculations
- 🎲 **Monte Carlo Simulations** - Assess retirement plan robustness with stochastic modeling
- 💼 **Multi-Account Support** - Model taxable, tax-deferred, and tax-exempt accounts
- 🔧 **Modern Tooling** - Built with `uv` for fast dependency management
- 📊 **Deterministic & Stochastic** - Run both predictable and probability-based projections
- 🧪 **Well-Tested** - Extensive test coverage with pytest
- 📝 **Type-Safe** - Full type hints for better IDE support

---

## 🎯 Features

### 🏦 Account Management
- **Taxable Accounts** - Standard brokerage accounts with capital gains tax
- **Tax-Deferred Accounts** - Traditional IRA/401k with income tax on withdrawal
- **Tax-Exempt Accounts** - Roth IRA/401k with tax-free growth and withdrawals

### 💰 German Tax Calculations (2025)
- Accurate German income tax brackets for single and married filers
- Capital gains tax (Abgeltungsteuer) at 26.375% including solidarity surcharge
- Automatic tax optimization during withdrawal strategies

### 📈 Retirement Simulations
- **Deterministic Projections** - Model retirement with fixed returns
- **Monte Carlo Analysis** - Run thousands of scenarios with variable returns
- **Success Rate Metrics** - Calculate probability of retirement goal achievement
- **Inflation Adjustment** - Automatic expense inflation over time

### 🎲 Stochastic Modeling
- Normal distribution returns with configurable mean and standard deviation
- Support for both growth and drawdown phases
- Multi-account withdrawal strategies with tax efficiency

### 📊 Results & Analytics
- Detailed year-by-year projections with Pandas DataFrames
- Account balance tracking across all account types
- Success rate calculations for retirement security

---

## 📦 Installation

### Using UV (Recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add finpy to your project
uv add finpy
```

### Using pip

```bash
pip install finpy
```

### Development Installation

```bash
# Clone the repository
git clone https://github.com/theAfricanQuant/finpy.git
cd finpy

# Install with development dependencies
uv sync --dev
```

---

## 🚀 Quick Start

### Basic Retirement Simulation

```python
from finpy.account import TaxableAccount, TaxDeferredAccount, TaxExemptAccount
from finpy.simulation import Portfolio, SimulationConfig, RetirementSimulator

# Set up your accounts with initial balances
taxable = TaxableAccount(balance=50000.0)
tax_deferred = TaxDeferredAccount(balance=200000.0)
tax_exempt = TaxExemptAccount(balance=100000.0)

portfolio = Portfolio(taxable, tax_deferred, tax_exempt)

# Configure your retirement scenario
config = SimulationConfig(
    current_age=30,
    retirement_age=65,
    end_age=95,
    annual_contribution=10000.0,
    retirement_expenses=50000.0,
    investment_return=0.07,  # 7% annual return
    investment_std_dev=0.15,  # 15% volatility
    inflation_rate=0.025,  # 2.5% inflation
    filing_status="single"
)

# Run the simulation
simulator = RetirementSimulator(portfolio, config)
results_df = simulator.run_deterministic_simulation()

print(results_df.head())
print(f"\nFinal Balance: €{results_df.iloc[-1]['Total']:,.2f}")
```

### Monte Carlo Analysis

```python
# Run 10,000 simulations to assess retirement security
monte_carlo_results = simulator.run_monte_carlo_simulation(iterations=10000)

print(f"Success Rate: {monte_carlo_results['success_rate']:.1%}")
print(f"Median Final Balance: €{sorted(monte_carlo_results['final_balances'])[5000]:,.2f}")
```

### Tax Calculations

```python
from finpy.taxes import calculate_income_tax, calculate_capital_gains_tax

# Calculate German income tax on withdrawal
income_tax = calculate_income_tax(income=80000.0, status="single")
print(f"Income Tax: €{income_tax:,.2f}")

# Calculate capital gains tax
cap_gains_tax = calculate_capital_gains_tax(gains=10000.0)
print(f"Capital Gains Tax: €{cap_gains_tax:,.2f}")
```

---

## 📚 Documentation

Comprehensive documentation is available at [finpy.readthedocs.io](https://finpy.readthedocs.io) (coming soon!)

### Project Structure

```
finpy/
├── src/finpy/          # Main package source code
│   ├── __init__.py
│   ├── account.py      # Account classes (Taxable, Tax-Deferred, Tax-Exempt)
│   ├── simulation.py   # Retirement simulator and portfolio management
│   ├── taxes.py        # German tax calculations (2025)
│   ├── utils.py        # Utility functions (inflation adjustment)
│   └── py.typed        # PEP 561 type marker
├── tests/              # Test suite
├── context/            # Project documentation
│   ├── PRD.md         # Product requirements
│   └── TASK.md        # Task breakdown
├── pyproject.toml      # Project configuration
└── README.md          # You are here!
```

---

## 🧪 Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=finpy --cov-report=html

# Run specific test file
uv run pytest tests/test_portfolio.py
```

### Code Quality

```bash
# Format code
uv run ruff format

# Lint code
uv run ruff check

# Fix auto-fixable issues
uv run ruff check --fix
```

### Type Checking

```bash
# Run type checker (if using mypy)
uv run mypy src/finpy
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. 🍴 Fork the repository
2. 🔨 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. ✅ Make your changes and add tests
4. 🧹 Ensure code quality (`uv run ruff check`)
5. 📝 Commit your changes (`git commit -m 'Add amazing feature'`)
6. 📤 Push to the branch (`git push origin feature/amazing-feature`)
7. 🎉 Open a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/finpy.git
cd finpy

# Install development dependencies
uv sync --dev

# Create a new branch
git checkout -b feature/your-feature-name
```

### Code Style

- Follow PEP 8 guidelines
- Use type hints for all functions
- Write docstrings for public APIs
- Maintain test coverage above 80%

---

## 📋 Requirements

- Python 3.14+
- Dependencies managed via `uv`

### Core Dependencies
- pandas - Data manipulation and analysis
- Python 3.14+ standard library (dataclasses, typing, random, copy)

### Development Dependencies
- pytest - Testing framework
- ruff - Linting and formatting
- Additional tools as needed

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🌟 Star History

If you find FinPy useful, please consider giving it a star! ⭐

---

## 🙏 Acknowledgments

- Built with [uv](https://github.com/astral-sh/uv) - The modern Python package installer
- Linted with [ruff](https://github.com/astral-sh/ruff) - An extremely fast Python linter
- Tested with [pytest](https://pytest.org) - Makes it easy to write tests

---

## 📞 Contact & Support

- 📧 **Issues**: [GitHub Issues](https://github.com/theAfricanQuant/finpy/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/theAfricanQuant/finpy/discussions)
- 🐦 **Twitter**: [@theAfricanQuant](https://twitter.com/theAfricanQuant)

---

<div align="center">

**Made with ❤️ by the FinPy Team**

[⬆ Back to Top](#-finpy)

</div>
