id: 6866d721317a06187fa55a21_documentation
summary: Portfolio Management Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Building a Portfolio Management Application with Streamlit: QuLab

## 1. Introduction to QuLab: Fundamentals of Portfolio Management
Duration: 0:05

Welcome to **QuLab**, an interactive Streamlit application designed to demystify key concepts in portfolio management, with a specific focus on risk assessment, asset allocation, and portfolio optimization. This codelab will guide you through the application's structure, functionalities, and the underlying financial principles it demonstrates.

In the dynamic world of finance, effective portfolio management is crucial for achieving investment goals while managing risk. An integral part of this process is understanding and defining an investor's **risk tolerance**, which dictates how investments are structured. This application provides a hands-on approach to concepts inspired by foundational documents like "Basics of Portfolio Planning and Construction," particularly concerning the assessment and visualization of risk.

**Key concepts you will explore:**
*   **Risk Profiling:** Assessing an investor's ability and willingness to take on investment risk. This involves both quantitative (financial situation) and qualitative (psychometric) factors.
*   **Investment Policy Statement (IPS):** Although not explicitly generated, the application lays the groundwork by helping define crucial components like risk objectives (absolute and relative).
*   **Asset Allocation:** The strategic distribution of investments across various asset classes (e.g., stocks, bonds, cash) to balance risk and return based on a defined risk tolerance.
*   **Portfolio Optimization:** The process of selecting the best portfolio (allocations) from a set of available assets, often aiming to maximize return for a given level of risk or minimize risk for a given return, frequently using frameworks like **Modern Portfolio Theory (MPT)** and metrics like the **Sharpe Ratio**.

This application serves as an excellent educational tool for developers and finance enthusiasts alike, allowing you to interact with core portfolio management principles and visualize their impact.

### Application Architecture Overview

The QuLab application is built using Streamlit, a powerful Python library for creating interactive web applications. It follows a modular design, separating different functionalities into distinct Python files for better organization and maintainability.

<aside class="positive">
A modular design enhances code readability, reusability, and makes it easier to extend the application with new features.
</aside>

Here's a high-level overview of the application's structure:

```mermaid
graph TD
    A[User Interaction in Browser] --> B[app.py (Main Application)]
    B -- Sidebar Navigation --> C{Page Selection}
    C -- "Risk Profiler" --> D[application_pages/page1.py]
    C -- "Asset Allocation" --> E[application_pages/page2.py]
    C -- "Portfolio Optimization" --> F[application_pages/page3.py]

    D --> G[Calculates Risk Profile & Visualizes Matrix]
    E --> H[Determines Allocation & Visualizes Pie Chart]
    F --> I[Performs Simplified Optimization & Visualizes Efficient Frontier]
```

## 2. Setting Up Your Development Environment
Duration: 0:10

To run the QuLab application locally, you need to set up your Python environment and install the necessary libraries.

### Prerequisites

*   Python 3.7+ installed on your system.
*   `pip` (Python package installer) installed and configured.

### 2.1. Clone the Application Code

First, ensure you have the application code structure. For this codelab, we'll assume you have the `app.py` file and the `application_pages` directory with `page1.py`, `page2.py`, and `page3.py` saved in a single root directory.

Let's visualize the required directory structure:

```
your-project-folder/
├── app.py
└── application_pages/
    ├── __init__.py (can be empty)
    ├── page1.py
    ├── page2.py
    └── page3.py
```

### 2.2. Install Dependencies

Open your terminal or command prompt, navigate to the `your-project-folder` directory, and install the required Python packages using `pip`.

```console
pip install streamlit plotly pandas numpy
```

<aside class="positive">
It's a good practice to use a virtual environment to manage project dependencies. This prevents conflicts with other Python projects on your system. You can create one using `python -m venv venv_name` and activate it.
</aside>

### 2.3. Run the Streamlit Application

Once all dependencies are installed, you can launch the Streamlit application.

```console
streamlit run app.py
```

Upon successful execution, Streamlit will open a new tab in your web browser, displaying the QuLab application. You will see the main interface with a sidebar for navigation.

## 3. Understanding the Risk Profiler (Page 1)
Duration: 0:15

The "Risk Profiler" is the first and foundational step in defining an investment strategy. It assesses an individual's **ability to bear risk** (financial capacity) and **willingness to take risk** (psychological comfort).

### 3.1. Code Overview: `application_pages/page1.py`

This file implements the logic for the Risk Profiler page.

```python
import streamlit as st
import plotly.graph_objects as go

def run_page1():
    st.header("Risk Profiler")
    st.markdown("""
    This page helps you understand your risk profile based on your financial situation and your willingness to take risks.
    We will assess your ability to bear risk and your willingness to take risk to determine your overall risk tolerance.
    The visual representation is inspired by "Exhibit 1: Risk Tolerance" (page 6) from the document "Basics of Portfolio Planning and Construction".
    """)

    st.subheader("A. Ability to Bear Risk Questionnaire (Financial Factors)")
    income = st.number_input('Annual Income ($)', value=50000)
    net_worth = st.number_input('Net Worth ($)', value=200000)
    liabilities = st.number_input('Total Liabilities ($)', value=50000)
    time_horizon = st.slider('Investment Time Horizon (Years)', min_value=1, max_value=30, value=10)
    dependents = st.slider('Number of Dependents', min_value=0, max_value=5, value=0)
    income_stability = st.selectbox('Income Stability', ['Stable', 'Fluctuating', 'Variable'])

    st.subheader("B. Willingness to Take Risk Assessment (Psychometric Factors)")
    q1 = st.slider('Question 1: "Investing is too difficult to understand." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q2 = st.slider('Question 2: "I get nervous when the stock market goes down." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q3 = st.slider('Question 3: "I am comfortable with the possibility of losing money on my investments." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)
    q4 = st.slider('Question 4: "I prefer investments with guaranteed returns, even if the returns are lower." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)
    q5 = st.slider('Question 5: "I actively seek out high-risk, high-reward investment opportunities." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)

    st.subheader("C. Risk Objective Definition")
    absolute_risk_objective = st.number_input('Maximum Acceptable Capital Loss (%)', min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    relative_risk_objective = st.number_input('Desired Benchmark Outperformance (%)', min_value=0.0, max_value=10.0, value=2.0, step=0.1)

    # Calculate Ability Score
    ability_score = (income / 10000) + (net_worth / 50000) - (liabilities / 20000) + (time_horizon / 10)
    min_conceptual_ability_score = -5
    max_conceptual_ability_score = 20
    ability_score_normalized = (ability_score - min_conceptual_ability_score) / (max_conceptual_ability_score - min_conceptual_ability_score)

    # Calculate Willingness Score
    willingness_score = q1 + q2 + q3 + q4 + q5

    # Determine Overall Risk Tolerance Category
    if ability_score_normalized < 0.5 and willingness_score < 15:
        risk_tolerance_category = "Below-average risk tolerance"
    elif ability_score_normalized >= 0.5 and willingness_score >= 15:
        risk_tolerance_category = "Above-average risk tolerance"
    else:
        risk_tolerance_category = "Resolution needed"

    st.subheader("Calculated Scores")
    st.markdown(f"Ability Score: {ability_score:.2f}")
    st.markdown(f"Normalized Ability Score: {ability_score_normalized:.2f}")
    st.markdown(f"Willingness Score: {willingness_score}")
    st.markdown(f"Overall Risk Tolerance Category: {risk_tolerance_category}")

    # Create Risk Tolerance Matrix (Scatter Plot)
    fig = go.Figure(data=go.Scatter(x=[ability_score_normalized], y=[willingness_score], mode='markers', marker=dict(size=20)))

    # Define Quadrant Boundaries
    x_boundary = 0.5
    y_boundary = 15

    # Add Quadrant Lines
    fig.add_vline(x=x_boundary, line_width=1, line_dash="dash", line_color="grey")
    fig.add_hline(y=y_boundary, line_width=1, line_dash="dash", line_color="grey")

    # Add Quadrant Annotations
    fig.add_annotation(x=0.25, y=7.5, text="Below-average risk tolerance", showarrow=False)
    fig.add_annotation(x=0.75, y=22.5, text="Above-average risk tolerance", showarrow=False)
    fig.add_annotation(x=0.25, y=22.5, text="Resolution needed", showarrow=False)
    fig.add_annotation(x=0.75, y=7.5, text="Resolution needed", showarrow=False)

    fig.update_layout(
        title="Client Risk Tolerance Matrix",
        xaxis_title="Normalized Ability to Bear Risk",
        yaxis_title="Willingness Score",
        xaxis_range=[0, 1],
        yaxis_range=[0, 25]
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Formulae")
    st.latex(r'	ext{Ability Score} = rac{	ext{Income}}{10000} + rac{	ext{Net Worth}}{50000} - rac{	ext{Liabilities}}{20000} + rac{	ext{Time Horizon}}{10}')
    st.latex(r'	ext{Ability Score Normalized} = rac{	ext{Ability Score} - 	ext{Min\_Conceptual\_Ability\_Score}}{	ext{Max\_Conceptual\_Ability\_Score} - 	ext{Min\_Conceptual\_Ability\_Score}}')
    st.latex(r'	ext{Willingness Score} = \sum_{i=1}^{5} 	ext{Psychometric Question Score}_i')
```

### 3.2. Core Functionalities and Concepts

1.  **Ability to Bear Risk:** This section collects financial inputs using Streamlit widgets like `st.number_input` and `st.slider`. These inputs include:
    *   Annual Income
    *   Net Worth
    *   Total Liabilities
    *   Investment Time Horizon
    *   Number of Dependents
    *   Income Stability
    The `ability_score` is calculated using a simple weighted sum, and then normalized to a scale between 0 and 1. This normalization makes it easier to compare and visualize.

    $$ \text{Ability Score} = \frac{\text{Income}}{10000} + \frac{\text{Net Worth}}{50000} - \frac{\text{Liabilities}}{20000} + \frac{\text{Time Horizon}}{10} $$
    $$ \text{Ability Score Normalized} = \frac{\text{Ability Score} - \text{Min\_Conceptual\_Ability\_Score}}{\text{Max\_Conceptual\_Ability\_Score} - \text{Min\_Conceptual\_Ability\_Score}} $$

2.  **Willingness to Take Risk:** This section uses `st.slider` widgets to gather responses to five psychometric questions. These questions are designed to gauge an individual's emotional comfort with investment volatility and potential losses. The `willingness_score` is simply the sum of responses to these questions.

    $$ \text{Willingness Score} = \sum_{i=1}^{5} \text{Psychometric Question Score}_i $$

3.  **Risk Objective Definition:** Investors often define specific risk objectives. This section allows users to input:
    *   **Maximum Acceptable Capital Loss (%):** An absolute risk objective.
    *   **Desired Benchmark Outperformance (%):** A relative risk objective.
    While these are not used in the risk category calculation within this page, they are crucial components of an IPS.

4.  **Overall Risk Tolerance Category:** Based on the calculated `normalized_ability_score` and `willingness_score`, the application categorizes the investor's overall risk tolerance into "Below-average risk tolerance," "Above-average risk tolerance," or "Resolution needed." The "Resolution needed" category highlights scenarios where the ability and willingness are mismatched, requiring further discussion or reconciliation.

5.  **Risk Tolerance Matrix Visualization:** A scatter plot generated using Plotly visualizes the client's position on a matrix, with "Normalized Ability to Bear Risk" on the x-axis and "Willingness Score" on the y-axis. Quadrant lines clearly delineate the different risk tolerance categories. This visual is powerful for understanding the interplay between financial capacity and psychological comfort.

### 3.3. Interacting with the Page

*   Navigate to the "Risk Profiler" page using the sidebar.
*   Adjust the financial inputs (income, net worth, etc.) and observe how the Ability Score changes.
*   Answer the psychometric questions by moving the sliders and see the impact on the Willingness Score.
*   Observe your dot on the "Client Risk Tolerance Matrix" and how it moves between quadrants based on your inputs.
*   Note the calculated `Overall Risk Tolerance Category` below the scores.

## 4. Deep Dive into Asset Allocation (Page 2)
Duration: 0:10

Once a risk profile is established, the next crucial step is **asset allocation** – deciding how to distribute investments among different asset classes. This page demonstrates a simplified model based on common risk tolerance levels.

### 4.1. Code Overview: `application_pages/page2.py`

This file handles the asset allocation logic and visualization.

```python
import streamlit as st
import plotly.graph_objects as go

def run_page2():
    st.header("Asset Allocation")
    st.markdown("""
    This page provides a basic asset allocation model based on your risk profile.
    The asset allocation is determined based on risk tolerance.
    """)

    risk_tolerance = st.selectbox("Select your risk tolerance:", ["Conservative", "Moderate", "Aggressive"])

    if risk_tolerance == "Conservative":
        stocks = 0.2
        bonds = 0.7
        cash = 0.1
    elif risk_tolerance == "Moderate":
        stocks = 0.5
        bonds = 0.4
        cash = 0.1
    else: # Aggressive
        stocks = 0.8
        bonds = 0.1
        cash = 0.1

    labels = ['Stocks', 'Bonds', 'Cash']
    values = [stocks, bonds, cash]

    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.update_layout(title_text="Asset Allocation", title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)

    st.markdown(f"""
    Based on a **{risk_tolerance}** risk tolerance, the recommended asset allocation is:
    - Stocks: {stocks*100:.0f}%
    - Bonds: {bonds*100:.0f}%
    - Cash: {cash*100:.0f}%
    """)
```

### 4.2. Core Functionalities and Concepts

1.  **Risk Tolerance Selection:** The page uses a `st.selectbox` to allow users to choose from three predefined risk tolerance levels: "Conservative," "Moderate," and "Aggressive."
    <aside class="positive">
    In a real-world scenario, the risk tolerance category determined in the "Risk Profiler" (Page 1) would automatically feed into this page, providing a more integrated user experience.
    </aside>

2.  **Predefined Allocations:** Based on the selected risk tolerance, the application assigns specific percentages to three primary asset classes: Stocks, Bonds, and Cash.
    *   **Conservative:** Higher allocation to bonds (lower risk), lower to stocks (higher potential return, higher risk).
    *   **Moderate:** Balanced allocation between stocks and bonds.
    *   **Aggressive:** Higher allocation to stocks (higher potential return, higher risk), lower to bonds.

3.  **Pie Chart Visualization:** Plotly is used to generate a pie chart (`go.Pie`) that visually represents the recommended asset allocation. The `hole=.3` parameter creates a donut chart, which is a common and aesthetically pleasing way to display portfolio breakdowns.

### 4.3. Interacting with the Page

*   Navigate to the "Asset Allocation" page.
*   Select different risk tolerance levels from the dropdown menu (Conservative, Moderate, Aggressive).
*   Observe how the pie chart and the displayed percentages for Stocks, Bonds, and Cash change according to the selected risk profile.

## 5. Exploring Portfolio Optimization (Page 3)
Duration: 0:15

**Portfolio Optimization** is the process of constructing a portfolio that maximizes expected return for a given level of risk, or minimizes risk for a given expected return. This page provides a simplified demonstration of this concept, drawing from **Modern Portfolio Theory (MPT)**.

### 5.1. Code Overview: `application_pages/page3.py`

This file contains the logic for a simplified portfolio optimization.

```python
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np # Ensure numpy is imported

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
    num_portfolios = 1000
    results = np.zeros((3,num_portfolios))
    optimal_weights = np.zeros(len(df)) # Initialize optimal_weights outside the loop
    max_sharpe = -np.inf # Initialize max_sharpe to a very small number

    for i in range(num_portfolios):
        weights = np.random.random(len(df)) # Generate random weights for all assets
        weights /= np.sum(weights) # Normalize weights to sum to 1

        portfolio_return = np.sum(df['Expected Return'].values * weights)
        # Convert covariances to numpy array for matrix multiplication
        portfolio_std = (weights @ np.array(covariances) @ weights)**0.5
        risk_free_rate = 0.01 # Define risk-free rate
        sharpe_ratio = (portfolio_return - risk_free_rate) / portfolio_std

        results[0,i] = portfolio_return
        results[1,i] = portfolio_std
        results[2,i] = sharpe_ratio

        # Update optimal portfolio if current sharpe ratio is higher
        if sharpe_ratio > max_sharpe:
            max_sharpe = sharpe_ratio
            optimal_weights = weights

    # Find the portfolio with the highest Sharpe ratio (from results array)
    max_sharpe_idx = np.argmax(results[2])
    optimal_return = results[0,max_sharpe_idx]
    optimal_std = results[1,max_sharpe_idx]
    optimal_sharpe = results[2,max_sharpe_idx]

    st.subheader("Optimal Portfolio")
    st.markdown(f"Optimal Expected Return: {optimal_return:.2f}")
    st.markdown(f"Optimal Risk (Volatility): {optimal_std:.2f}")
    st.markdown(f"Optimal Sharpe Ratio: {optimal_sharpe:.2f}")
    st.markdown(f"Optimal Weights: {optimal_weights}")

    # Create a scatter plot of portfolio risk vs return (Efficient Frontier)
    fig = px.scatter(x=results[1,:], y=results[0,:], color=results[2,:], labels={'x':'Risk', 'y':'Return', 'color':'Sharpe Ratio'})
    fig.add_scatter(x=[optimal_std], y=[optimal_return], mode='markers', marker=dict(color='red', size=12), name='Optimal Portfolio')
    fig.update_layout(title="Efficient Frontier with Optimal Portfolio", xaxis_title="Portfolio Risk (Standard Deviation)", yaxis_title="Portfolio Return")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Disclaimer:** This is a simplified example and does not constitute financial advice.
    Real-world portfolio optimization involves more complex models and data.
    """)
```

### 5.2. Core Functionalities and Concepts

1.  **Sample Asset Data:** The page starts with a DataFrame showing sample assets, their expected returns, and risk (volatility). In a real application, this data would come from historical market data analysis.

2.  **Sharpe Ratio:** A key metric in MPT, the Sharpe Ratio measures the risk-adjusted return of an investment or portfolio. It is defined as the average return earned in excess of the risk-free rate per unit of volatility (total risk). A higher Sharpe Ratio indicates a better risk-adjusted return.

    $$ \text{Sharpe Ratio} = \frac{E[R_p] - R_f}{\sigma_p} $$
    Where:
    *   $E[R_p]$ is the expected portfolio return
    *   $R_f$ is the risk-free rate
    *   $\sigma_p$ is the portfolio's standard deviation (volatility)

3.  **Covariance Matrix:** This matrix is crucial for calculating portfolio standard deviation. It measures how much two assets move in tandem. The formula for portfolio standard deviation with weights $w$ and covariance matrix $\Sigma$ is:
    $$ \sigma_p = \sqrt{w^T \Sigma w} $$

4.  **Simplified Brute-Force Optimization:** For demonstration, the application generates a large number of random portfolio weight combinations (`num_portfolios`). For each combination, it calculates:
    *   **Portfolio Return:** $E[R_p] = \sum_{i} w_i \cdot E[R_i]$
    *   **Portfolio Standard Deviation (Risk):** Using the covariance matrix and weights.
    *   **Sharpe Ratio:** Using the formula above.
    The portfolio with the highest Sharpe Ratio among these random combinations is identified as the "optimal portfolio."

    <aside class="negative">
    This brute-force method is computationally inefficient for a large number of assets. Real-world portfolio optimization uses sophisticated numerical optimization techniques (e.g., using `scipy.optimize` in Python) to find truly optimal solutions.
    </aside>

5.  **Efficient Frontier Visualization:** A scatter plot (`plotly.express.scatter`) is generated where the x-axis represents Portfolio Risk (Standard Deviation) and the y-axis represents Portfolio Return. Each point on the plot represents a randomly generated portfolio. The color of the point indicates its Sharpe Ratio. The curve formed by the portfolios with the highest return for each level of risk is known as the **Efficient Frontier**. The optimal portfolio (highest Sharpe Ratio) is highlighted in red on this plot.

### 5.3. Interacting with the Page

*   Navigate to the "Portfolio Optimization" page.
*   Review the sample asset data.
*   Observe the "Optimal Portfolio" metrics (Return, Risk, Sharpe Ratio, and Weights).
*   Examine the "Efficient Frontier" plot. The red marker indicates the simulated optimal portfolio, which represents the best risk-adjusted return given the sample assets and simplified optimization.

## 6. Extending and Customizing QuLab
Duration: 0:10

QuLab provides a robust foundation for understanding portfolio management. As a developer, you can extend its functionalities to create a more sophisticated and real-world application.

### 6.1. Potential Enhancements

*   **Integrate Real-Time Market Data:** Instead of sample data, fetch historical stock prices, returns, and volatilities from financial APIs (e.g., Yahoo Finance, Alpha Vantage) using libraries like `yfinance` or `pandas_datareader`.
*   **Advanced Risk Profiling:**
    *   Implement more comprehensive psychometric tests with validated questionnaires.
    *   Incorporate qualitative factors like market outlook, specific investment constraints, or ethical considerations.
    *   Automatically link the output of the risk profiler to the asset allocation page.
*   **Sophisticated Portfolio Optimization:**
    *   Implement proper numerical optimization techniques using libraries like `scipy.optimize` to find the true Efficient Frontier and optimal portfolios (e.g., for maximum Sharpe Ratio, minimum variance, or target return).
    *   Allow users to define custom constraints (e.g., maximum allocation per asset, no short-selling).
    *   Add more advanced risk measures like Value-at-Risk (VaR) or Conditional Value-at-Risk (CVaR).
*   **Diverse Asset Classes:** Expand beyond stocks, bonds, and cash to include commodities, real estate, alternative investments, etc.
*   **Performance Tracking:** Add a module to track the performance of a simulated portfolio over time against benchmarks.
*   **Scenario Analysis/Stress Testing:** Allow users to simulate how their portfolio would perform under different market conditions (e.g., recessions, boom periods).
*   **User Authentication and Portfolio Saving:** For a multi-user application, implement user login and the ability to save/load individual portfolio configurations.
*   **Improved User Experience:**
    *   Add tooltips and more detailed explanations for financial terms.
    *   Implement Streamlit's session state to persist user inputs across pages or reruns.

### 6.2. Streamlit Development Best Practices

*   **Modularity:** Keep your code organized in separate files for different functionalities, as demonstrated in this application (`application_pages`).
*   **Session State:** For more complex applications where user inputs need to persist across reruns or page navigations, utilize `st.session_state`.
*   **Caching:** Use `st.cache_data` or `st.cache_resource` for functions that fetch data or perform heavy computations that don't change frequently. This significantly improves performance.
*   **Error Handling:** Implement robust error handling for API calls or complex calculations.
*   **Responsiveness:** Streamlit applications are generally responsive, but ensure your visualizations adapt well to different screen sizes.

By leveraging Streamlit's simplicity and Python's powerful libraries for data science and finance, you can transform this basic QuLab into a comprehensive tool for financial analysis and education.

<button>
  [Download App.py and Pages](https://github.com/your-repo/qu-lab-streamlit/archive/main.zip)
</button>
(Note: The above link is a placeholder. Replace with an actual download link if hosted.)
