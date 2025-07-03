
import streamlit as st
import plotly.graph_objects as go
import numpy as np

def run_page1():
    st.header("Interactive Risk Profiler")

    st.markdown("""
    This section allows you to assess your risk tolerance based on your financial situation and psychological preferences.  Enter your information in the fields below to generate your risk profile. The tooltips provide additional guidance and references to the "Basics of Portfolio Planning and Construction" document.
    """)

    st.subheader("A. Ability to Bear Risk (Financial Factors)")
    st.markdown("""
    Enter your financial information to assess your ability to bear risk. This section considers objective factors such as income, net worth, and time horizon.
    """)

    income = st.number_input('Annual Income ($)', value=50000, help="Your annual income. Higher income generally indicates a greater ability to bear risk.")
    net_worth = st.number_input('Net Worth ($)', value=200000, help="Your total assets minus your total liabilities. Higher net worth generally indicates a greater ability to bear risk.")
    liabilities = st.number_input('Total Liabilities ($)', value=50000, help="Your total debts. Higher liabilities generally indicate a lower ability to bear risk.")
    time_horizon = st.slider('Investment Time Horizon (Years)', min_value=1, max_value=30, value=10, help="The length of time you plan to invest. A longer time horizon generally indicates a greater ability to bear risk.")
    dependents = st.slider('Number of Dependents', min_value=0, max_value=5, value=0, help="The number of people who rely on your financial support. More dependents generally indicate a lower ability to bear risk.")
    income_stability = st.selectbox('Income Stability', ['Stable', 'Fluctuating', 'Variable'], help="The consistency of your income. Stable income generally indicates a greater ability to bear risk.")

    st.subheader("B. Willingness to Take Risk (Psychometric Factors)")
    st.markdown("""
    Answer the following questions to assess your willingness to take risk.  These questions gauge your psychological attitude towards investment risks.
    """)

    q1 = st.slider('Question 1: "Investing is too difficult to understand." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q2 = st.slider('Question 2: "I get anxious when the stock market declines." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q3 = st.slider('Question 3: "I am comfortable with the possibility of losing money on my investments." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)
    q4 = st.slider('Question 4: "I tend to make conservative investment choices." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)
    q5 = st.slider('Question 5: "I enjoy taking risks in other areas of my life." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)

    # Calculate Ability Score
    ability_score = (income / 10000) + (net_worth / 50000) - (liabilities / 20000) + (time_horizon / 10)

    # Define Min and Max Conceptual Ability Score
    min_conceptual_ability_score = -5  # Example minimum value
    max_conceptual_ability_score = 20 # Example maximum value

    # Normalize Ability Score to a range between 0 and 1
    ability_score_normalized = (ability_score - min_conceptual_ability_score) / (max_conceptual_ability_score - min_conceptual_ability_score)
    ability_score_normalized = np.clip(ability_score_normalized, 0, 1) # Ensure the value is within 0 and 1

    # Calculate Willingness Score
    willingness_score = q1 + q2 + q3 + q4 + q5

    st.subheader("C. Risk Objective Definition")
    st.markdown("""
    Define your investment objectives in terms of maximum acceptable loss and desired outperformance relative to a benchmark.
    """)

    absolute_risk_objective = st.number_input('Maximum Acceptable Capital Loss (%)', min_value=0.0, max_value=100.0, value=5.0, step=0.1, help="The maximum percentage of your investment that you are willing to lose.")
    relative_risk_objective = st.number_input('Desired Benchmark Outperformance (%)', min_value=0.0, max_value=10.0, value=2.0, step=0.1, help="The percentage by which you want your investments to outperform a benchmark.")

    # Determine Risk Tolerance Category
    if ability_score_normalized < 0.5 and willingness_score < 15:
        risk_tolerance_category = "Below-average risk tolerance"
    elif ability_score_normalized >= 0.5 and willingness_score >= 15:
        risk_tolerance_category = "Above-average risk tolerance"
    else:
        risk_tolerance_category = "Resolution needed"

    st.subheader("Risk Profile")

    st.markdown("""
    **Ability Score:** $rac{	ext{Income}}{10000} + rac{	ext{Net Worth}}{50000} - rac{	ext{Liabilities}}{20000} + rac{	ext{Time Horizon}}{10}$
    """)
    st.markdown(f"**Ability Score:** {ability_score:.2f}")

    st.markdown("""
    **Ability Score Normalized:** $rac{	ext{Ability Score} - 	ext{Min\_Conceptual\_Ability\_Score}}{	ext{Max\_Conceptual\_Ability\_Score} - 	ext{Min\_Conceptual\_Ability\_Score}}$
    """)

    st.markdown(f"**Ability Score Normalized:** {ability_score_normalized:.2f}")
    st.markdown(f"**Willingness Score:** {willingness_score}")
    st.markdown(f"**Overall Risk Tolerance Category:** {risk_tolerance_category}")

    # Create Scatter Plot
    fig = go.Figure(data=go.Scatter(x=[ability_score_normalized], y=[willingness_score], mode='markers', marker=dict(size=[20])))

    fig.update_layout(
        title='Client Risk Tolerance Matrix',
        xaxis_title='Normalized Ability to Bear Risk',
        yaxis_title='Willingness Score',
        xaxis=dict(range=[0, 1]),
        yaxis=dict(range=[5, 25]),
        annotations=[
            dict(x=0.25, y=10, text='Below-average risk tolerance', showarrow=False),
            dict(x=0.75, y=10, text='Resolution needed', showarrow=False),
            dict(x=0.25, y=20, text='Resolution needed', showarrow=False),
            dict(x=0.75, y=20, text='Above-average risk tolerance', showarrow=False)
        ]
    )

    st.plotly_chart(fig, use_container_width=True)
