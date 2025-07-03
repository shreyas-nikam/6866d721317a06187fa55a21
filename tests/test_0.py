import pytest
import pandas as pd
import numpy as np

# Placeholder for the module import
from definition_f435f085715f4e67a389a18f0a701d94 import generate_synthetic_client_data

# Define a set of expected core columns based on the notebook specification.
# These represent financial factors and psychometric responses.
# The actual implementation might have more columns, but these should be present.
EXPECTED_CORE_COLUMNS = [
    'income',
    'net_worth',
    'liabilities',
    'time_horizon',
    'dependents',
    'income_stability', # Expected to be categorical or string
    'psychometric_q1',
    'psychometric_q2',
    'psychometric_q3',
    'psychometric_q4',
    'psychometric_q5'
]

def test_generate_synthetic_client_data_return_type():
    """
    Test that the function returns a pandas DataFrame for valid inputs.
    """
    df = generate_synthetic_client_data(num_clients=1, seed=None)
    assert isinstance(df, pd.DataFrame)

@pytest.mark.parametrize("num_clients, seed, expected_rows", [
    # Valid cases for num_clients and seed
    (1, None, 1),
    (5, 42, 5),
    (100, 123, 100),
    (1000, None, 1000), # Test with a larger number of clients

    # Edge cases: num_clients = 0
    (0, None, 0),
    (0, 99, 0),
])
def test_generate_synthetic_client_data_valid_inputs_and_structure(num_clients, seed, expected_rows):
    """
    Test various valid combinations of num_clients and seed,
    and verify the structure of the returned DataFrame.
    """
    df = generate_synthetic_client_data(num_clients=num_clients, seed=seed)

    assert isinstance(df, pd.DataFrame)
    assert len(df) == expected_rows

    if expected_rows > 0:
        assert not df.empty
        # All expected core columns should be present
        assert all(col in df.columns for col in EXPECTED_CORE_COLUMNS), \
            f"Missing expected columns in DataFrame: {[col for col in EXPECTED_CORE_COLUMNS if col not in df.columns]}"
        
        # Check for non-null values in some critical columns (assuming they shouldn't be null)
        for col in ['income', 'net_worth', 'time_horizon', 'psychometric_q1']:
            if col in df.columns: # Defensive check
                assert df[col].isnull().sum() == 0, f"Column '{col}' contains null values."
    else: # For num_clients = 0
        assert df.empty
        # An empty DataFrame should still have columns defined
        assert len(df.columns) > 0, "Empty DataFrame should still have columns defined."
        # The schema of the empty DataFrame should match the expected core columns
        assert all(col in df.columns for col in EXPECTED_CORE_COLUMNS), \
            f"Missing expected columns in empty DataFrame: {[col for col in EXPECTED_CORE_COLUMNS if col not in df.columns]}"


def test_generate_synthetic_client_data_reproducibility_with_seed():
    """
    Test that providing the same seed produces identical results,
    and different seeds produce different results.
    """
    num_clients = 50
    seed_val_1 = 42
    seed_val_2 = 42
    seed_val_3 = 100

    df_a = generate_synthetic_client_data(num_clients=num_clients, seed=seed_val_1)
    df_b = generate_synthetic_client_data(num_clients=num_clients, seed=seed_val_2)
    df_c = generate_synthetic_client_data(num_clients=num_clients, seed=seed_val_3)

    # DataFrames generated with the same seed must be identical
    pd.testing.assert_frame_equal(df_a, df_b)

    # DataFrames generated with different seeds should ideally be different
    # Use try-except to catch AssertionError as direct equality might rarely occur by chance,
    # but the intent is to verify non-reproducibility without the same seed.
    with pytest.raises(AssertionError):
        pd.testing.assert_frame_equal(df_a, df_c)


@pytest.mark.parametrize("num_clients, seed, expected_exception", [
    # Invalid num_clients type (must be int)
    (1.5, None, TypeError),
    ("abc", None, TypeError),
    ([1, 2], None, TypeError),
    (None, None, TypeError), # num_clients is a required argument, None is invalid type

    # Invalid num_clients value (must be non-negative)
    (-1, None, ValueError),
    (-10, 42, ValueError),
])
def test_generate_synthetic_client_data_invalid_num_clients_inputs(num_clients, seed, expected_exception):
    """
    Test that the function raises appropriate exceptions for invalid num_clients inputs.
    """
    with pytest.raises(expected_exception):
        generate_synthetic_client_data(num_clients=num_clients, seed=seed)


@pytest.mark.parametrize("num_clients, seed, expected_exception", [
    # Invalid seed type (must be int or None)
    (5, 1.5, TypeError),
    (5, "bad_seed", TypeError),
    (5, [1], TypeError),
    (5, {'key': 'value'}, TypeError),
])
def test_generate_synthetic_client_data_invalid_seed_type(num_clients, seed, expected_exception):
    """
    Test that the function raises TypeError for invalid seed types (when not None).
    """
    with pytest.raises(expected_exception):
        generate_synthetic_client_data(num_clients=num_clients, seed=seed)

def test_generate_synthetic_client_data_column_data_types():
    """
    Test that the columns in the generated DataFrame have expected data types.
    Financial values should be numeric, psychometric scores typically integer,
    and categorical like 'income_stability' could be object/string/category.
    """
    df = generate_synthetic_client_data(num_clients=10, seed=123)
    assert not df.empty

    # Check financial columns for numeric types
    numeric_financial_cols = ['income', 'net_worth', 'liabilities', 'time_horizon', 'dependents']
    for col in numeric_financial_cols:
        if col in df.columns:
            assert pd.api.types.is_numeric_dtype(df[col]), f"Column '{col}' is not numeric."
            # Further check for integer/float depending on expected precision
            # For simplicity, just numeric for now.

    # Check psychometric columns for integer types (assuming scores are integers)
    psychometric_score_cols = [f'psychometric_q{i}' for i in range(1, 6)]
    for col in psychometric_score_cols:
        if col in df.columns:
            assert pd.api.types.is_integer_dtype(df[col]), f"Column '{col}' is not integer."

    # Check categorical/string column
    if 'income_stability' in df.columns:
        assert pd.api.types.is_string_dtype(df['income_stability']) or \
               pd.api.types.is_categorical_dtype(df['income_stability']), \
               f"Column 'income_stability' is not string or categorical."