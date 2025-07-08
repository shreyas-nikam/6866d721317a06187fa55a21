
import pytest
import pandas as pd
from <your_module> import generate_synthetic_client_data

# Define expected columns for the generated DataFrame based on the notebook specification.
# These include financial factors and a score from psychometric responses.
EXPECTED_COLUMNS = [
    'annual_income', 'income_stability', 'net_worth', 'total_liabilities',
    'investment_time_horizon', 'dependents', 'willingness_score'
]

@pytest.mark.parametrize(
    "num_clients, expected_output_type, expected_rows, expected_error_type, expected_error_message_match",
    [
        # Test Case 1: Valid positive input (multiple clients)
        (5, pd.DataFrame, 5, None, None),
        # Test Case 2: Zero clients (edge case)
        (0, pd.DataFrame, 0, None, None),
        # Test Case 3: Single client (edge case)
        (1, pd.DataFrame, 1, None, None),
        # Test Case 4: Negative num_clients (edge case - invalid value)
        (-1, None, None, ValueError, "num_clients must be a non-negative integer"),
        # Test Case 5: Non-integer num_clients (edge case - invalid type: float)
        (3.5, None, None, TypeError, "num_clients must be an integer"),
    ]
)
def test_generate_synthetic_client_data(num_clients, expected_output_type, expected_rows, expected_error_type, expected_error_message_match):
    if expected_error_type:
        # If an error is expected, assert that the correct exception is raised
        with pytest.raises(expected_error_type, match=expected_error_message_match):
            generate_synthetic_client_data(num_clients)
    else:
        # If no error is expected, assert the DataFrame properties
        df = generate_synthetic_client_data(num_clients)
        assert isinstance(df, expected_output_type), f"Expected output type {expected_output_type}, but got {type(df)}"
        assert len(df) == expected_rows, f"Expected {expected_rows} rows, but got {len(df)}"

        # Check for the presence of all expected columns in the DataFrame
        # This check is crucial for both non-empty and 0-row DataFrames to ensure correct schema.
        assert all(col in df.columns for col in EXPECTED_COLUMNS), \
            f"DataFrame is missing one or more expected columns. Expected: {EXPECTED_COLUMNS}, Got: {df.columns.tolist()}"

        # For non-empty DataFrames, assert that there are no null values and check data types.
        if expected_rows > 0:
            assert not df.isnull().any().any(), "Generated DataFrame contains unexpected null values"

            # Check data types and value ranges for numeric columns
            numeric_cols = ['annual_income', 'net_worth', 'total_liabilities', 'investment_time_horizon', 'dependents', 'willingness_score']
            for col in numeric_cols:
                if col in df.columns: # Defensive check, though covered by previous assert
                    assert pd.api.types.is_numeric_dtype(df[col]), f"Column '{col}' is not numeric"
                    # All these numeric columns are expected to be non-negative based on financial context.
                    assert (df[col] >= 0).all(), f"Column '{col}' contains negative values"

            # Check data types and validity for categorical column 'income_stability'
            if 'income_stability' in df.columns: # Defensive check
                valid_stability_categories = ['Very Stable', 'Stable', 'Volatile']
                assert pd.api.types.is_string_dtype(df['income_stability']) or pd.api.types.is_object_dtype(df['income_stability']), \
                    "Column 'income_stability' is not string/object type"
                assert df['income_stability'].isin(valid_stability_categories).all(), \
                    "Column 'income_stability' contains invalid categories"
