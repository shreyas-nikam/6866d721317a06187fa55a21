
import streamlit as st
import plotly.express as px
import pandas as pd

def run_page3():
    st.header("Portfolio Optimization")
    st.markdown("""
    This page demonstrates a simplified portfolio optimization based on Modern Portfolio Theory (MPT).
    It uses a sample dataset of asset returns to find the portfolio with the highest Sharpe ratio.
    """)

    # Sample Data (replace with actual data)
    data = {
        'Asset': ['Asset A', 'Asset B', 'Asset C'],
        'Expected Return': [0.10, 0.15, 0.20],
        'Risk (Volatility)': [0.15, 0.20, 0.25]
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

    # Portfolio Optimization (Simplified)
    def calculate_sharpe_ratio(weights, expected_returns, covariances, risk_free_rate=0.01):
        portfolio_return = sum(weights * expected_returns)
        portfolio_std = (weights @ covariances @ weights)**0.5
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std
        return sharpe_ratio

    # Example Covariance Matrix
    covariances = [
        [0.0225, 0.015, 0.01875],
        [0.015, 0.04, 0.025],
        [0.01875, 0.025, 0.0625]
    ]

    # Brute-force optimization (for demonstration)
    import numpy as np
    num_portfolios = 1000
    results = np.zeros((3,num_portfolios))
    for i in range(num_portfolios):
        weights = np.random.random(3)
        weights /= np.sum(weights) # Normalize weights

        portfolio_return = np.sum(df['Expected Return'] * weights)
        portfolio_std = (weights @ covariances @ weights)**0.5
        sharpe_ratio = (portfolio_return - 0.01) / portfolio_std

        results[0,i] = portfolio_return
        results[1,i] = portfolio_std
        results[2,i] = sharpe_ratio

    # Find the portfolio with the highest Sharpe ratio
    max_sharpe_idx = np.argmax(results[2])
    optimal_weights = weights
    optimal_return = results[0,max_sharpe_idx]
    optimal_std = results[1,max_sharpe_idx]
    optimal_sharpe = results[2,max_sharpe_idx]

    st.subheader("Optimal Portfolio")
    st.markdown(f"Optimal Expected Return: {optimal_return:.2f}")
    st.markdown(f"Optimal Risk (Volatility): {optimal_std:.2f}")
    st.markdown(f"Optimal Sharpe Ratio: {optimal_sharpe:.2f}")
    st.markdown(f"Optimal Weights: {optimal_weights}")

    # Create a scatter plot of portfolio risk vs return
    fig = px.scatter(x=results[1,:], y=results[0,:], color=results[2,:], labels={'x':'Risk', 'y':'Return', 'color':'Sharpe Ratio'})
    fig.add_scatter(x=[optimal_std], y=[optimal_return], marker={'color':'red', 'size':12}, name='Optimal Portfolio')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Disclaimer:** This is a simplified example and does not constitute financial advice.
    Real-world portfolio optimization involves more complex models and data.
    """)
