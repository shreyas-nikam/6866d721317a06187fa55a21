
import pytest
import pandas as pd
import numpy as np

from <your_module> import generate_synthetic_client_data

# Define the expected columns in the synthetic DataFrame based on the specification:
# "financial details (income, wealth, liabilities, time horizon)" and
# "psychometric questionnaire responses" (e.g., 5 questions).
# These column names are aligned with common practices and the likely structure from the problem context.
EXPECTED_COLUMNS = [
    'client_id',
    'annual_income',
    'income_stability',         # e.g., categorical: 'Very Stable', 'Stable', 'Volatile'
    'net_worth',
    'total_liabilities',
    'investment_time_horizon',  # e.g., in years
    'num_dependents',
    'questionnaire_q1',         # Scores from psychometric questions (e.g., 1-4)
    'questionnaire_q2',
    'questionnaire_q3',
    'questionnaire_q4',
    'questionnaire_q5'
]

@pytest.mark.parametrize(
    "num_clients, seed, expected_exception, check_reproducibility",
    [
        # Test Case 1: Basic functionality - generates multiple clients with a specific seed.
        # Verifies DataFrame type, correct shape (rows and columns), and presence of expected columns.
        (10, 42, None, False),

        # Test Case 2: Edge case - generates zero clients.
        # Should return an an empty DataFrame but still with the correct column structure.
        (0, None, None, False),

        # Test Case 3: Invalid input - negative 'num_clients'.
        # Expects a ValueError as client count cannot be negative.
        (-5, None, ValueError, False),

        # Test Case 4: Invalid input - non-integer 'num_clients'.
        # Expects a TypeError as 'num_clients' should be an integer type.
        (10.5, None, TypeError, False),

        # Test Case 5: Reproducibility - verifies that the same seed produces identical datasets.
        # This test case calls the function twice with the same parameters and compares the outputs.
        (5, 123, None, True),
    ]
)
def test_generate_synthetic_client_data(num_clients, seed, expected_exception, check_reproducibility):
    if expected_exception:
        # If an exception is expected, assert that the function raises it.
        with pytest.raises(expected_exception):
            generate_synthetic_client_data(num_clients, seed)
    elif check_reproducibility:
        # For reproducibility tests, call the function twice with the same seed
        # and assert that the resulting DataFrames are identical.
        df1 = generate_synthetic_client_data(num_clients, seed)
        df2 = generate_synthetic_client_data(num_clients, seed)

        assert isinstance(df1, pd.DataFrame)
        assert isinstance(df2, pd.DataFrame)
        # Ensure correct shape before comparing content
        assert df1.shape == (num_clients, len(EXPECTED_COLUMNS))
        assert df2.shape == (num_clients, len(EXPECTED_COLUMNS))
        pd.testing.assert_frame_equal(df1, df2)
    else:
        # For successful generation scenarios, perform general checks on the output DataFrame.
        df = generate_synthetic_client_data(num_clients, seed)

        assert isinstance(df, pd.DataFrame)
        # Verify the DataFrame has the expected number of rows and columns.
        assert df.shape == (num_clients, len(EXPECTED_COLUMNS))
        # Verify all expected columns are present in the DataFrame.
        # Using set comparison for robustness against column order
        assert set(df.columns) == set(EXPECTED_COLUMNS)

        # For non-empty DataFrames, perform additional checks on data types and value ranges.
        if num_clients > 0:
            assert not df.empty
            # Check basic data types for some key financial and questionnaire columns.
            # These checks assume common numerical data types for financial metrics.
            assert pd.api.types.is_numeric_dtype(df['annual_income'])
            assert pd.api.types.is_numeric_dtype(df['net_worth'])
            assert pd.api.types.is_numeric_dtype(df['total_liabilities'])
            assert pd.api.types.is_integer_dtype(df['investment_time_horizon'])
            assert pd.api.types.is_integer_dtype(df['num_dependents'])
            assert pd.api.types.is_integer_dtype(df['client_id'])

            # Check psychometric question scores are integers and within the expected range (e.g., 1 to 4).
            for i in range(1, 6):
                q_col = f'questionnaire_q{i}'
                assert pd.api.types.is_integer_dtype(df[q_col])
                # As per spec (Exhibit 2, Page 6-7), scores typically 1 to 4.
                assert df[q_col].min() >= 1
                assert df[q_col].max() <= 4

            # 'income_stability' is described as categorical (e.g., 'Very Stable', 'Stable', 'Volatile').
            # It should be an object (string) dtype.
            assert pd.api.types.is_object_dtype(df['income_stability']) or pd.api.types.is_string_dtype(df['income_stability'])
            # Optional: Further check if values are within expected categories if specific generation logic is known:
            # allowed_stability_categories = {'Very Stable', 'Stable', 'Volatile'}
            # assert df['income_stability'].isin(allowed_stability_categories).all()
