import pytest
import pandas as pd
from definition_60d8cb40686f46c991d4f06442a156f8 import generate_synthetic_client_data

@pytest.mark.parametrize("num_clients, expected_type, expected_rows, expected_exception, expected_columns", [
    # Valid positive integer inputs
    (1, pd.DataFrame, 1, None, ['annual_income', 'net_worth', 'total_liabilities', 'time_horizon_years', 'income_stability', 'q1_response', 'q2_response', 'q3_response', 'q4_response', 'q5_response']),
    (5, pd.DataFrame, 5, None, ['annual_income', 'net_worth', 'total_liabilities', 'time_horizon_years', 'income_stability', 'q1_response', 'q2_response', 'q3_response', 'q4_response', 'q5_response']),
    (100, pd.DataFrame, 100, None, ['annual_income', 'net_worth', 'total_liabilities', 'time_horizon_years', 'income_stability', 'q1_response', 'q2_response', 'q3_response', 'q4_response', 'q5_response']),
    # Edge case: num_clients = 0
    (0, pd.DataFrame, 0, None, []), # For 0 clients, columns might be an empty list or specific empty columns
    # Invalid input types
    (3.14, None, None, TypeError, None),
    ("abc", None, None, TypeError, None),
    (None, None, None, TypeError, None),
    ([1, 2], None, None, TypeError, None),
    ({'a': 1}, None, None, TypeError, None),
    # Invalid input values
    (-1, None, None, ValueError, None),
    (-10, None, None, ValueError, None),
])
def test_generate_synthetic_client_data(num_clients, expected_type, expected_rows, expected_exception, expected_columns):
    """
    Tests the generate_synthetic_client_data function for various valid and invalid inputs.
    """
    if expected_exception:
        with pytest.raises(expected_exception) as excinfo:
            generate_synthetic_client_data(num_clients)
        # Optional: Check message if specific error messages are expected
        # assert "expected part of error message" in str(excinfo.value)
    else:
        df = generate_synthetic_client_data(num_clients)

        # Check return type
        assert isinstance(df, expected_type)

        # Check number of rows
        assert len(df) == expected_rows

        # Check columns for non-empty DataFrame
        if expected_rows > 0:
            # Check if all expected columns are present
            assert all(col in df.columns for col in expected_columns)
            # Ensure no unexpected columns either, assuming a fixed schema
            assert len(df.columns) == len(expected_columns)
            
            # Check data types of generated columns (optional, but good for robustness)
            # This depends on the internal implementation of synthetic data generation.
            # Example checks:
            assert pd.api.types.is_numeric_dtype(df['annual_income'])
            assert pd.api.types.is_numeric_dtype(df['net_worth'])
            assert pd.api.types.is_numeric_dtype(df['total_liabilities'])
            assert pd.api.types.is_integer_dtype(df['time_horizon_years'])
            assert pd.api.types.is_string_dtype(df['income_stability'])
            
            # Check psychometric questionnaire responses are reasonable (e.g., within 1-4 or 1-5 range)
            for i in range(1, 6): # Assuming 5 questions as per spec
                assert pd.api.types.is_integer_dtype(df[f'q{i}_response'])
                assert df[f'q{i}_response'].min() >= 1
                assert df[f'q{i}_response'].max() <= 4 # Assuming 4 options as per spec

        # Check for empty DataFrame case
        if expected_rows == 0:
            assert df.empty
            # For an empty DataFrame, columns might be defined but empty, or truly empty.
            # The spec implies a consistent schema, even for 0 rows, but depends on implementation.
            # Let's assume an empty DataFrame will still have the column names, just no data.
            # If the implementation returns pd.DataFrame() (no columns), adjust this.
            # Here, we'll check if the *expected* columns (if any for an empty df) are present.
            # Given my `expected_columns` for 0 rows is `[]`, this check passes.
            # If `generate_synthetic_client_data(0)` *should* return df with `['annual_income', ...]`
            # but 0 rows, then `expected_columns` for 0 would be the full list.
            # For now, let's assume a truly empty df for 0 clients.
            # If the function creates an empty df with specified columns:
            # assert list(df.columns) == ['annual_income', 'net_worth', 'total_liabilities', 'time_horizon_years', 'income_stability', 'q1_response', 'q2_response', 'q3_response', 'q4_response', 'q5_response']
            pass # No specific column checks needed for a truly empty df here