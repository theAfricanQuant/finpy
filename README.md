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

**FinPy** is a powerful, modern Python library designed for financial analysis, quantitative finance, and algorithmic trading. Built with performance and ease-of-use in mind, FinPy provides a comprehensive toolkit for financial professionals, data scientists, and quantitative analysts.

### ✨ Key Highlights

- 🎯 **Intuitive API** - Clean, Pythonic interface for complex financial calculations
- ⚡ **High Performance** - Optimized for speed and efficiency
- 🔧 **Modern Tooling** - Built with `uv` for fast dependency management
- 📈 **Comprehensive** - From basic metrics to advanced quantitative models
- 🧪 **Well-Tested** - Extensive test coverage with pytest
- 📝 **Type-Safe** - Full type hints for better IDE support

---

## 🎯 Features

### 📉 Financial Analysis
- Portfolio analytics and optimization
- Risk metrics and performance attribution
- Asset pricing models
- Time series analysis

### 💹 Market Data
- Data fetching and processing
- Technical indicators
- Market microstructure analysis

### 🎲 Quantitative Models
- Options pricing (Black-Scholes, binomial models)
- Fixed income analytics
- Statistical arbitrage strategies
- Risk modeling (VaR, CVaR)

### 🛠️ Utilities
- Financial calendar utilities
- Data validation and cleaning
- Visualization helpers

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

```python
from finpy import Portfolio, Stock

# Create a portfolio
portfolio = Portfolio()

# Add positions
portfolio.add_position(Stock("AAPL"), quantity=100, price=150.0)
portfolio.add_position(Stock("GOOGL"), quantity=50, price=2800.0)

# Calculate metrics
print(f"Total Value: ${portfolio.total_value():,.2f}")
print(f"Returns: {portfolio.returns():.2%}")
print(f"Sharpe Ratio: {portfolio.sharpe_ratio():.2f}")
```

### More Examples

```python
from finpy.options import BlackScholes
from finpy.risk import calculate_var

# Option pricing
call_price = BlackScholes.call(
    spot=100,
    strike=105,
    time_to_expiry=0.25,
    risk_free_rate=0.05,
    volatility=0.20
)

# Risk analysis
var_95 = calculate_var(returns, confidence=0.95)
```

---

## 📚 Documentation

Comprehensive documentation is available at [finpy.readthedocs.io](https://finpy.readthedocs.io) (coming soon!)

### Project Structure

```
finpy/
├── src/finpy/          # Main package source code
│   ├── __init__.py
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
- Will be listed as the project develops

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
