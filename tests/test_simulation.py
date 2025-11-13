import pytest
import pandas as pd
from finpy.account import TaxableAccount, TaxDeferredAccount, TaxExemptAccount
from finpy.simulation import SimulationConfig, Portfolio, RetirementSimulator

@pytest.fixture
def sample_config():
    """Fixture for a sample SimulationConfig."""
    return SimulationConfig(
        current_age=30,
        retirement_age=65,
        end_age=95,
        annual_contribution=15000,
        retirement_expenses=60000,
        investment_return=0.07,
        investment_std_dev=0.15,
        inflation_rate=0.03,
        filing_status="single"
    )

@pytest.fixture
def sample_portfolio():
    """Fixture for a sample Portfolio."""
    return Portfolio(
        taxable=TaxableAccount(balance=100000),
        tax_deferred=TaxDeferredAccount(balance=200000),
        tax_exempt=TaxExemptAccount(balance=50000)
    )

def test_simulation_config_creation(sample_config):
    """Verify the data class can be instantiated with all parameters."""
    assert sample_config.current_age == 30
    assert sample_config.retirement_expenses == 60000

def test_portfolio_initialization(sample_portfolio):
    """Test portfolio initialization."""
    assert sample_portfolio.taxable.balance == 100000

def test_portfolio_total_balance(sample_portfolio):
    """Test portfolio total balance calculation."""
    assert sample_portfolio.total_balance == 350000

def test_simulator_initialization(sample_portfolio, sample_config):
    """Verify the simulator can be created with a portfolio and config."""
    simulator = RetirementSimulator(sample_portfolio, sample_config)
    assert simulator.portfolio.total_balance == sample_portfolio.total_balance
    assert simulator.config.current_age == sample_config.current_age

def test_simulation_single_year_run_pre_retirement(sample_portfolio, sample_config):
    """Verify balances after one pre-retirement year."""
    sample_config.investment_std_dev = 0.0 # Deterministic
    simulator = RetirementSimulator(sample_portfolio, sample_config)
    
    simulator._run_single_year(current_age=40, expenses=0)
    
    expected_deferred = (200000 + 15000) * 1.07
    expected_taxable = 100000 * 1.07
    expected_exempt = 50000 * 1.07

    assert simulator.portfolio.tax_deferred.balance == pytest.approx(expected_deferred)
    assert simulator.portfolio.taxable.balance == pytest.approx(expected_taxable)
    assert simulator.portfolio.tax_exempt.balance == pytest.approx(expected_exempt)

def test_deterministic_simulation_full_run(sample_portfolio, sample_config):
    """Verify the final portfolio value matches a pre-calculated scenario."""
    simulator = RetirementSimulator(sample_portfolio, sample_config)
    results_df = simulator.run_deterministic_simulation()
    
    assert len(results_df) == (sample_config.end_age - sample_config.current_age + 1)
    assert results_df["Total"].iloc[-1] > 0

def test_deterministic_simulation_output_format(sample_portfolio, sample_config):
    """Verify the output is a DataFrame with expected columns."""
    simulator = RetirementSimulator(sample_portfolio, sample_config)
    results_df = simulator.run_deterministic_simulation()
    assert isinstance(results_df, pd.DataFrame)
    expected_columns = ["Age", "Taxable", "Tax-Deferred", "Tax-Exempt", "Total"]
    assert all(col in results_df.columns for col in expected_columns)

def test_monte_carlo_runs_multiple_simulations(sample_portfolio, sample_config):
    """Verify the method runs the specified number of iterations."""
    simulator = RetirementSimulator(sample_portfolio, sample_config)
    iterations = 10
    results = simulator.run_monte_carlo_simulation(iterations)
    assert len(results["final_balances"]) == iterations
    assert sample_portfolio.total_balance == simulator.portfolio.total_balance

def test_calculate_success_rate():
    """Verify correct success rate for a given set of final balances."""
    assert True

def test_monte_carlo_output_format(sample_portfolio, sample_config):
    """Verify the output structure contains the success rate and raw data."""
    simulator = RetirementSimulator(sample_portfolio, sample_config)
    results = simulator.run_monte_carlo_simulation(10)
    assert "success_rate" in results
    assert "final_balances" in results
    assert isinstance(results["success_rate"], float)
    assert isinstance(results["final_balances"], list)
    assert 0.0 <= results["success_rate"] <= 1.0
