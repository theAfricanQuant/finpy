# PyTire Development Tasks

This document outlines the development tasks for building the PyTire library, based on the PRD. All tasks should be completed following Test-Driven Development (TDD).

## Phase 1: Core Financial Modeling Engine (F1)

### Account Modeling (FR1.1)
- [ ] 1. Create a base `Account` class that holds a balance.
- [ ] 2. Create `TaxableAccount`, `TaxDeferredAccount`, and `TaxExemptAccount` classes inheriting from the base `Account`.

### Cash Flow & Growth (FR1.2, FR1.3, FR1.4)
- [ ] 3. Implement `deposit` and `withdraw` methods on the base `Account` class.
- [ ] 4. Implement a `project_growth` method on the base `Account` class to apply a deterministic annual return.
- [ ] 5. Create a utility function to apply inflation to a given value.

## Phase 2: Tax Calculation Module (German) (F2)

### Tax Configuration & Calculation (FR2.1, FR2.2, FR2.3)
- [ ] 6. Create data structures to hold configurable German tax brackets for 2025 (Single and Married Filing Jointly).
- [ ] 7. Implement a function to calculate German income tax for a given taxable income and "Single" filing status.
- [ ] 8. Extend the income tax function to support "Married Filing Jointly" status.
- [ ] 9. Implement a function to calculate German capital gains tax.

## Phase 3: Simulation and Analysis (F3 & F4)

### Configuration and Setup (FR4.1, FR4.2)
- [ ] 10. Create a `SimulationConfig` data class to hold all user inputs (ages, balances, contributions, etc.).
- [ ] 11. Create a `Portfolio` class to hold and manage the different account types (`Taxable`, `TaxDeferred`, `TaxExempt`).

### Deterministic Simulation (FR3.1)
- [ ] 12. Create a `RetirementSimulator` class that takes a `Portfolio` and `SimulationConfig`.
- [ ] 13. Implement the main simulation loop for a single year within the simulator, which coordinates contributions, expenses, growth, and tax calculations.
- [ ] 14. Implement the `run_deterministic_simulation` method to run the annual loop from the current age to the end age.
- [ ] 15. Ensure the deterministic simulation results are returned as a pandas DataFrame (FR3.4).

### Monte Carlo Simulation (FR3.2, FR3.3)
- [ ] 16. Modify the `project_growth` method in the `Account` class to handle stochastic returns using a mean and standard deviation.
- [ ] 17. Implement the `run_monte_carlo_simulation` method to execute the simulation multiple times with stochastic returns.
- [ ] 18. Implement the success rate calculation based on the Monte Carlo results.
- [ ] 19. Ensure Monte Carlo simulation results (success rate and raw data) are returned in a structured format (FR3.4).
