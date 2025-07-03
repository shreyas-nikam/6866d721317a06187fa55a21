
import pandas as pd
import numpy as np
from typing import Optional, Dict, Any

def generate_synthetic_client_data(num_clients: int, seed: Optional[int] = None) -> pd.DataFrame:
    """
    Generates a synthetic dataset of client financial details and hypothetical psychometric
    questionnaire responses for demonstration purposes. This data mimics various financial
    profiles and risk attitudes, serving as a controlled environment for testing the application.

    Arguments:
        num_clients (int): The number of synthetic client profiles to generate.
        seed (int, optional): A seed for the random number generator to ensure reproducibility.
                              Defaults to None.

    Output:
        pandas.DataFrame: A DataFrame containing synthetic client data with columns for
                          financial factors and questionnaire responses.
    """
    # Define the expected columns and their intended dtypes.
    # This ensures consistency, especially for the case where num_clients = 0.
    COLUMN_DTYPES: Dict[str, Any] = {
        'income': float,
        'net_worth': float,
        'liabilities': float,
        'time_horizon': int,
        'dependents': int,
        'income_stability': 'category',  # Using 'category' for type clarity and efficiency
        'psychometric_q1': int,
        'psychometric_q2': int,
        'psychometric_q3': int,
        'psychometric_q4': int,
        'psychometric_q5': int
    }
    
    # 1. Error Handling and Input Validation
    if not isinstance(num_clients, int):
        raise TypeError(f"num_clients must be an integer, got {type(num_clients).__name__}.")
    if num_clients < 0:
        raise ValueError("num_clients must be a non-negative integer.")

    if seed is not None and not isinstance(seed, int):
        raise TypeError(f"seed must be an integer or None, got {type(seed).__name__}.")

    # 2. Handle the edge case of 0 clients
    if num_clients == 0:
        # Create an empty DataFrame with the correct schema (columns and dtypes)
        df = pd.DataFrame(columns=list(COLUMN_DTYPES.keys()))
        for col, dtype in COLUMN_DTYPES.items():
            df[col] = df[col].astype(dtype)
        return df

    # 3. Initialize Random Number Generator for reproducibility
    # Changed from np.random.default_rng to np.random.RandomState
    # to align with reported AttributeError regarding 'randint' method,
    # as RandomState objects use randint, while Generator objects use integers.
    rng = np.random.RandomState(seed)

    # 4. Generate Synthetic Data
    data: Dict[str, Any] = {}

    # Financial Factors
    # Income: Skewed positive distribution (e.g., log-normal to represent income distribution)
    data['income'] = np.round(rng.lognormal(mean=10.5, sigma=0.7, size=num_clients), 2)
    # Net Worth: Can be positive or negative (normal distribution)
    data['net_worth'] = np.round(rng.normal(loc=150000, scale=100000, size=num_clients), 2)
    # Liabilities: Positive values, ensure non-negative after generation
    liabilities_raw = np.round(rng.normal(loc=70000, scale=40000, size=num_clients), 2)
    data['liabilities'] = np.maximum(liabilities_raw, 0) # Ensure liabilities are non-negative

    # Time Horizon: Integer, e.g., 1 to 30 years (inclusive of 1 and 30)
    # Changed from .integers to .randint (high is exclusive, so 31 means up to 30)
    data['time_horizon'] = rng.randint(1, 31, size=num_clients)
    # Dependents: Integer, e.g., 0 to 5 (inclusive of 0 and 5)
    # Changed from .integers to .randint (high is exclusive, so 6 means up to 5)
    data['dependents'] = rng.randint(0, 6, size=num_clients)

    # Income Stability: Categorical (e.g., Stable, Fluctuating, Variable)
    income_stability_options = ['Stable', 'Fluctuating', 'Variable']
    data['income_stability'] = rng.choice(income_stability_options, size=num_clients)

    # Psychometric Questionnaire Responses (Likert Scale 1-5, inclusive of 1 and 5)
    for i in range(1, 6):
        # Changed from .integers to .randint (high is exclusive, so 6 means up to 5)
        data[f'psychometric_q{i}'] = rng.randint(1, 6, size=num_clients)

    # 5. Create DataFrame and enforce data types
    df = pd.DataFrame(data)

    # Ensure columns have the specified dtypes
    for col, dtype in COLUMN_DTYPES.items():
        if col in df.columns:
            # Using .astype() directly handles type conversions efficiently for all specified dtypes.
            df[col] = df[col].astype(dtype)

    return df
