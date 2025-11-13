# PyTire Development Tasks

This document outlines the development tasks for building the PyTire library, based on the PRD. All tasks should be completed following Test-driven Development (TDD).

## Phase 0: Project Setup
- [x] 0. Create the `tests` directory to house all test files.

## Phase 1: Core Financial Modeling Engine (F1)

### Account Modeling (FR1.1)
- [x] 1. Create a base `Account` class that holds a balance.
    - **Test:** `test_account_initialization`: Verify an account can be created with an initial balance.
- [x] 2. Create `TaxableAccount`, `TaxDeferredAccount`, and `TaxExemptAccount` classes inheriting from the base `Account`.
    - **Test:** `test_account_subclass_creation`: Verify instances of each subclass can be created correctly.

### Cash Flow & Growth (FR1.2, FR1.3, FR1.4)
- [x] 3. Implement `deposit` and `withdraw` methods on the base `Account` class.
    - **Tests:** `test_deposit_increases_balance`, `test_withdraw_decreases_balance`, `test_withdraw_raises_error_on_insufficient_funds`.
- [x] 4. Implement a `project_growth` method on the base `Account` class to apply a deterministic annual return.
    - **Test:** `test_project_growth_increases_balance`: Verify balance is correctly increased by the return rate.
- [ ] 5. Create a utility function to apply inflation to a given value.
    - **Test:** `test_apply_inflation`: Verify a value is correctly reduced by the inflation rate.

## Phase 2: Tax Calculation Module (German) (F2)

### Tax Configuration & Calculation (FR2.1, FR2.2, FR2.3)
- [ ] 6. Create data structures to hold configurable German tax brackets for 2025 (Single and Married Filing Jointly).
    - **Test:** `test_tax_brackets_structure`: Verify the data structure loads correctly and contains expected keys.
- [ ] 7. Implement a function to calculate German income tax for a given taxable income and "Single" filing status.
    - **Test:** `test_calculate_income_tax_single`: Test incomes in various brackets, at bracket boundaries, and zero income.
- [ ] 8. Extend the income tax function to support "Married Filing Jointly" status.
    - **Test:** `test_calculate_income_tax_married`: Test incomes in various brackets for the joint status.
- [ ] 9. Implement a function to calculate German capital gains tax.
    - **Test:** `test_calculate_capital_gains_tax`: Verify the calculation with various capital gain amounts.

## Phase 3: Simulation and Analysis (F3 & F4)

### Configuration and Setup (FR4.1, FR4.2)
- [ ] 10. Create a `SimulationConfig` data class to hold all user inputs (ages, balances, contributions, etc.).
    - **Test:** `test_simulation_config_creation`: Verify the data class can be instantiated with all parameters.
- [ ] 11. Create a `Portfolio` class to hold and manage the different account types (`Taxable`, `TaxDeferred`, `TaxExempt`).
    - **Tests:** `test_portfolio_initialization`, `test_portfolio_total_balance`.

### Deterministic Simulation (FR3.1)
- [ ] 12. Create a `RetirementSimulator` class that takes a `Portfolio` and `SimulationConfig`.
    - **Test:** `test_simulator_initialization`: Verify the simulator can be created with a portfolio and config.
- [ ] 13. Implement the main simulation loop for a single year within the simulator, which coordinates contributions, expenses, growth, and tax calculations.
    - **Test:** `test_simulation_single_year_run`: Verify end-of-year balances are correct after one cycle of all events.
- [ ] 14. Implement the `run_deterministic_simulation` method to run the annual loop from the current age to the end age.
    - **Test:** `test_deterministic_simulation_full_run`: Verify the final portfolio value matches a pre-calculated scenario.
- [ ] 15. Ensure the deterministic simulation results are returned as a pandas DataFrame (FR3.4).
    - **Test:** `test_deterministic_simulation_output_format`: Verify the output is a DataFrame with expected columns.

### Monte Carlo Simulation (FR3.2, FR3.3)
- [ ] 16. Modify the `project_growth` method in the `Account` class to handle stochastic returns using a mean and standard deviation.
    - **Test:** `test_project_stochastic_growth`: Verify the method uses a random number generator and handles volatility.
- [ ] 17. Implement the `run_monte_carlo_simulation` method to execute the simulation multiple times with stochastic returns.
    - **Test:** `test_monte_carlo_runs_multiple_simulations`: Verify the method runs the specified number of iterations.
- [ ] 18. Implement the success rate calculation based on the Monte Carlo results.
    - **Test:** `test_calculate_success_rate`: Verify correct success rate for a given set of final balances.
- [ ] 19. Ensure Monte Carlo simulation results (success rate and raw data) are returned in a structured format (FR3.4).
    - **Test:** `test_monte_carlo_output_format`: Verify the output structure contains the success rate and raw data.
