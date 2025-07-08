import pytest
import pandas as pd
import numpy as np

# Placeholder for the module import
from definition_d37224e67b5041bca97b723cc93edaaa import generate_synthetic_client_data

# Define expected columns based on the notebook specification's implied data schema.
# These are inferred from the description of financial profiles and psychometric responses.
# The exact names might vary in the actual implementation, but these are reasonable guesses
# to ensure the generated DataFrame contains the necessary information.
EXPECTED_COLUMNS = [
    'Annual Income',
    'Net Worth',
    'Total Liabilities',
    'Investment Time Horizon', # e.g., years
    'Income Stability',        # e.g., 'Very Stable', 'Stable', 'Volatile'
    'Dependents',
    'Willingness Q1',          # Psychometric question 1 score (e.g., 1-4)
    'Willingness Q2',
    'Willingness Q3',
    'Willingness Q4',
    'Willingness Q5',
    # Additional columns, like a calculated 'Willingness Score' or 'Ability Score',
    # might be present but are not strictly required for the *generation* function's output.
]

def test_generate_synthetic_client_data_return_type():
    """
    Test that the function returns a pandas DataFrame.
    """
    df = generate_synthetic_client_data(num_clients=5, seed=42)
    assert isinstance(df, pd.DataFrame), "The function should return a pandas DataFrame."

@pytest.mark.parametrize("num_clients, seed", [
    (5, 42),       # Standard valid input
    (1, 123),      # Single client
    (100, 789),    # Larger number of clients
    (10, None),    # Test with None for seed (should use default random state)
    (0, 99),       # Zero clients (should return an empty DataFrame)
])
def test_generate_synthetic_client_data_valid_inputs_and_shape(num_clients, seed):
    """
    Test with various valid numbers of clients and seeds,
    and verify the resulting DataFrame's shape and basic content.
    """
    df = generate_synthetic_client_data(num_clients=num_clients, seed=seed)

    assert df.shape[0] == num_clients, \
        f"DataFrame should have {num_clients} rows for num_clients={num_clients}."

    if num_clients > 0:
        # For non-empty DataFrames, check for expected columns and non-null values
        for col in EXPECTED_COLUMNS:
            assert col in df.columns, f"Column '{col}' missing from DataFrame for num_clients={num_clients}."
        
        # Ensure that the DataFrame is not entirely empty of data for valid inputs
        assert not df.empty, "DataFrame should not be empty when num_clients > 0."
        
        # Optionally, check that there are no unexpected columns (beyond a reasonable tolerance)
        # This might be too strict if the implementation adds internal/derived columns.
        # assert len(df.columns) == len(EXPECTED_COLUMNS), "DataFrame has an unexpected number of columns."
        
    else: # num_clients == 0
        assert df.empty, "DataFrame should be empty when num_clients is 0."
        assert df.columns.tolist() == [], "Empty DataFrame should have no columns when num_clients is 0."


@pytest.mark.parametrize("num_clients, expected_exception", [
    (-1, ValueError),    # Negative number of clients
    (-100, ValueError),  # Another negative number
    (1.5, TypeError),    # Float as num_clients
    ("five", TypeError), # String as num_clients
    ([5], TypeError),    # List as num_clients
    (True, TypeError),   # Boolean as num_clients
    (False, TypeError),  # Boolean as num_clients
])
def test_generate_synthetic_client_data_invalid_num_clients_type_or_value(num_clients, expected_exception):
    """
    Test that invalid num_clients inputs (negative values, wrong types)
    raise the appropriate exceptions (ValueError for negative, TypeError for wrong type).
    """
    with pytest.raises(expected_exception):
        generate_synthetic_client_data(num_clients=num_clients, seed=42)

@pytest.mark.parametrize("seed, expected_exception", [
    ("invalid_seed", TypeError), # String as seed (should be int or None)
    (3.14, TypeError),           # Float as seed
    ([1,2,3], TypeError),        # List as seed
    ({'a':1}, TypeError),        # Dictionary as seed
    (True, TypeError),           # Boolean as seed
])
def test_generate_synthetic_client_data_invalid_seed_type(seed, expected_exception):
    """
    Test that invalid seed inputs (wrong types) raise the appropriate TypeError.
    """
    # Use a valid num_clients to isolate the seed validation
    with pytest.raises(expected_exception):
        generate_synthetic_client_data(num_clients=5, seed=seed)

def test_generate_synthetic_client_data_reproducibility():
    """
    Test that the function produces identical results when called with the same seed and num_clients.
    """
    num_clients = 20
    seed = 88

    df1 = generate_synthetic_client_data(num_clients=num_clients, seed=seed)
    df2 = generate_synthetic_client_data(num_clients=num_clients, seed=seed)

    pd.testing.assert_frame_equal(df1, df2, check_dtype=True)

def test_generate_synthetic_client_data_non_reproducibility_different_seed():
    """
    Test that the function produces different results when called with different seeds,
    for the same num_clients.
    This test expects an AssertionError from pd.testing.assert_frame_equal, indicating
    the DataFrames are indeed different.
    """
    num_clients = 20

    df1 = generate_synthetic_client_data(num_clients=num_clients, seed=100)
    df2 = generate_synthetic_client_data(num_clients=num_clients, seed=101) # Different seed

    with pytest.raises(AssertionError):
        pd.testing.assert_frame_equal(df1, df2)

def test_generate_synthetic_client_data_column_data_types_and_ranges():
    """
    Test that generated columns have plausible data types and their values fall within
    expected (though illustrative) ranges, based on the notebook specification.
    This checks the quality and realism of the generated data.
    """
    df = generate_synthetic_client_data(num_clients=100, seed=55)
    assert not df.empty, "DataFrame should not be empty for this test."

    # Validate financial columns' data types and ranges
    assert df['Annual Income'].dtype in [np.int64, np.float64], "Annual Income should be numeric."
    assert df['Net Worth'].dtype in [np.int64, np.float64], "Net Worth should be numeric."
    assert df['Total Liabilities'].dtype in [np.int64, np.float64], "Total Liabilities should be numeric."
    assert df['Investment Time Horizon'].dtype == np.int64, "Investment Time Horizon should be integer (years)."
    assert df['Dependents'].dtype == np.int64, "Dependents should be integer."

    # Illustrative ranges (can be adjusted based on the actual synthetic data generation logic)
    assert df['Annual Income'].min() >= 15000 and df['Annual Income'].max() <= 1_500_000
    assert df['Net Worth'].min() >= -100_000 and df['Net Worth'].max() <= 10_000_000
    assert df['Total Liabilities'].min() >= 0 and df['Total Liabilities'].max() <= 3_000_000
    assert df['Investment Time Horizon'].min() >= 1 and df['Investment Time Horizon'].max() <= 60 # Years
    assert df['Dependents'].min() >= 0 and df['Dependents'].max() <= 10 # Number of dependents

    # Validate categorical column
    assert df['Income Stability'].dtype == 'object' or pd.api.types.is_categorical_dtype(df['Income Stability']), \
        "Income Stability should be object or categorical."
    expected_stability_categories = {'Very Stable', 'Stable', 'Volatile'}
    assert set(df['Income Stability'].unique()).issubset(expected_stability_categories), \
        "Income Stability contains unexpected categories."

    # Validate psychometric questionnaire columns
    for i in range(1, 6): # Assuming 5 questions based on spec
        col_name = f'Willingness Q{i}'
        assert col_name in df.columns, f"Psychometric question column '{col_name}' is missing."
        assert df[col_name].dtype == np.int64, f"'{col_name}' should be integer (score)."
        # Check scores are within the typical 1-4 range as implied by Exhibit 2
        assert df[col_name].min() >= 1 and df[col_name].max() <= 4, \
            f"'{col_name}' scores out of expected range (1-4)."