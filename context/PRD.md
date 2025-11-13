# Product Requirements Document (PRD): PyTire

## 1. Introduction

**PyTire** is a Python library for sophisticated retirement and tax planning simulations. It provides a transparent, customizable, and powerful framework for modeling an individual's financial journey into retirement, accounting for investment growth, taxes, and different account structures.

*   **Problem**: Planning for retirement is complex. Individuals must account for taxes, inflation, market volatility, and the rules governing various retirement accounts (401k, IRA, Roth, etc.). Commercial tools are often expensive "black boxes," while simpler calculators lack the necessary detail for robust planning.
*   **Solution**: PyTire will be an open-source library that empowers users to run detailed, personalized financial simulations. By providing a clear and extensible API, it will serve as a foundational tool for personal use, financial advisors, and developers building fintech applications.
*   **Target Audience**:
    *   DIY investors and financially literate individuals who want to model their own retirement scenarios.
    *   Financial advisors seeking a flexible, programmable tool for client analysis.
    *   Python developers building custom financial planning and analysis applications.

## 2. Goals & Objectives

*   **Prime Directive**: You will NOT PROCEED with any task if you have any questions. Please ask and verify any concerns. Only proceed when you are clear as to what to do.
*   **Model Comprehensive Financial Scenarios**: Accurately simulate portfolio growth across different account types (taxable, tax-deferred, tax-exempt).
*   **Integrate Tax Planning**: Model the tax implications of contributions, growth, and withdrawals according to current (2025) German federal tax law.
*   **Assess Retirement Viability**: Use simulation techniques like Monte Carlo analysis to determine the probability of a successful retirement plan.
*   **Provide a Flexible API**: Offer a clean, well-documented, and extensible Python API that is easy to configure and integrate into other projects.

## 3. Features & Functional Requirements

### F1: Core Financial Modeling Engine
*   **FR1.1: Account Modeling**: The library must support the three primary types of investment accounts:
    *   Taxable (e.g., standard brokerage account).
    *   Tax-Deferred (e.g., Traditional 401k/IRA).
    *   Tax-Exempt (e.g., Roth 401k/IRA).
*   **FR1.2: Growth Projection**: Project investment growth based on user-configurable parameters like average annual return and standard deviation.
*   **FR1.3: Cash Flow Simulation**: Model annual cash flows, including income, savings contributions, and retirement expenses.
*   **FR1.4: Inflation Modeling**: Account for inflation to adjust future expenses and model real (inflation-adjusted) returns.

### F2: Tax Calculation Module (German)
*   **FR2.1: Income Tax**: Implement the German federal income tax bracket system for calculating taxes on income and traditional account withdrawals. Must support "Single" and "Married Filing Jointly" statuses.
*   **FR2.2: Capital Gains Tax**: Implement long-term capital gains tax calculations for withdrawals from taxable brokerage accounts.
*   **FR2.3: Configurable Tax Laws**: Tax brackets and rates should be configurable to allow for easy updates as tax laws change. (Note: State taxes are out of scope for MVP).

### F3: Simulation and Analysis
*   **FR3.1: Deterministic Projection**: Run a straight-line projection showing the year-by-year balance of each account until a target end age (e.g., 100).
*   **FR3.2: Monte Carlo Simulation**: Perform stochastic simulations using Monte Carlo methods to model a range of potential outcomes based on market volatility.
*   **FR3.3: Success Rate Calculation**: Based on Monte Carlo results, calculate the probability that the portfolio will not be depleted before the end of the plan (i.e., the "success rate").
*   **FR3.4: Data Output**: The results of a simulation run (both deterministic and Monte Carlo) must be returned in a structured format, such as a pandas DataFrame, for easy analysis and visualization by the user.

### F4: User Configuration
*   **FR4.1**: All simulation parameters must be configurable via Python objects or a simple configuration file (e.g., YAML).
*   **FR4.2**: Key inputs shall include: current age, retirement age, life expectancy, current balances in each account type, annual contribution amounts, planned retirement expenses, and assumptions for investment returns and inflation.

## 4. Non-Functional Requirements

*   **Accuracy**: Financial calculations (e.g., compound growth, tax liabilities) must be precise and validated against known benchmarks.
*   **Performance**: A simulation of a 60-year timeline with 1,000 Monte Carlo iterations should complete in under 30 seconds.
*   **Testability**: The codebase must have extensive unit test coverage (target >90%) to ensure the correctness of calculations.
*   **Documentation**: The project must include comprehensive API documentation with clear examples for common use cases.
*   **Extensibility**: The library's architecture should be modular, allowing users to extend it with custom models (e.g., different country's tax systems, more complex withdrawal strategies).

## 5. Coding Standards

*   use Python. Lay-out is: 
```
finpy
├── context
│   └── PRD.md
├── pyproject.toml
├── README.md
├── src
│   └── finpy
│       ├── __init__.py
```
*   Use TDD.
*   since we are using uv and zshell, activate the .venv by running `activate_venv` as a zsh command to help with the activation.
*   Write tests before each task. 
*   Do not mock. 
*   use SOLID best practices. 
*   We will be using pytest to test. Add type hints

## 6. Future Scope (Post-MVP)

*   Modeling of Social Security and pension benefits.
*   Support for Required Minimum Distributions (RMDs).
*   Modeling advanced withdrawal strategies (e.g., Roth conversion ladders).
*   Inclusion of Nigerian Federal income tax calculations on diaspora accounts.
*   Helper functions for generating common visualizations (e.g., portfolio balance over time, distribution of Monte Carlo outcomes).
