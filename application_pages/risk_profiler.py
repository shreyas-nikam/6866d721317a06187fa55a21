
import streamlit as st
import plotly.express as px
import pandas as pd

def run_risk_profiler():
    st.header("Risk Profiler")

    # --- Ability to Bear Risk Questionnaire (Financial Factors) ---
    st.subheader("Financial Factors (Ability to Bear Risk)")
    income = st.number_input('Annual Income ($)', value=50000)
    net_worth = st.number_input('Net Worth ($)', value=250000)
    liabilities = st.number_input('Total Liabilities ($)', value=50000)
    time_horizon = st.slider('Investment Time Horizon (Years)', min_value=1, max_value=30, value=10)
    dependents = st.slider('Number of Dependents', min_value=0, max_value=5, value=2)
    income_stability = st.selectbox('Income Stability', ['Stable', 'Fluctuating', 'Variable'])

    # --- Willingness to Take Risk Assessment (Psychometric Factors) ---
    st.subheader("Psychometric Factors (Willingness to Take Risk)")
    q1 = st.slider('Question 1: "Investing is too difficult to understand." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q2 = st.slider('Question 2: "I get anxious when the market fluctuates." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q3 = st.slider('Question 3: "I prefer investments with guaranteed returns, even if the returns are lower." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q4 = st.slider('Question 4: "I am comfortable with the possibility of losing money on my investments." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)
    q5 = st.slider('Question 5: "I like to take risks in other areas of my life." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)

    # --- Calculations ---
    ability_score = (income / 10000) + (net_worth / 50000) - (liabilities / 20000) + (time_horizon / 10)
    min_conceptual_ability_score = -5  # Example minimum value
    max_conceptual_ability_score = 20 # Example maximum value

    ability_score_normalized = (ability_score - min_conceptual_ability_score) / (max_conceptual_ability_score - min_conceptual_ability_score)
    willingness_score = (6 - q1) + (6 - q2) + (6 - q3) + q4 + q5 # Inverting the first three questions so that higher score is higher willingness

    # --- Risk Tolerance Category ---
    if ability_score_normalized < 0.5 and willingness_score < 15:
        risk_tolerance_category = "Below-average risk tolerance"
    elif ability_score_normalized >= 0.5 and willingness_score >= 15:
        risk_tolerance_category = "Above-average risk tolerance"
    else:
        risk_tolerance_category = "Resolution needed"

    # --- Display Calculated Scores ---
    st.subheader("Calculated Scores")
    st.markdown(f"Ability Score: {ability_score:.2f}")
    st.markdown(f"Normalized Ability Score: {ability_score_normalized:.2f}")
    st.markdown(f"Willingness Score: {willingness_score}")
    st.markdown(f"Overall Risk Tolerance Category: {risk_tolerance_category}")

    # --- Risk Objective Definition ---
    st.subheader("Risk Objective Definition")
    absolute_risk_objective = st.number_input('Maximum Acceptable Capital Loss (%)', min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    relative_risk_objective = st.number_input('Desired Benchmark Outperformance (%)', min_value=0.0, max_value=10.0, value=2.0, step=0.1)

    # --- Visualization ---
    st.subheader("Client Risk Tolerance Matrix")

    # Create a dataframe for the scatter plot
    data = {'Ability': [ability_score_normalized], 'Willingness': [willingness_score], 'Category': [risk_tolerance_category]}
    df = pd.DataFrame(data)

    # Define quadrants
    quadrants = {
        "Below-average risk tolerance": {'Ability': 0.25, 'Willingness': 7.5},
        "Resolution needed (Low Ability)": {'Ability': 0.25, 'Willingness': 22.5},
        "Resolution needed (High Ability)": {'Ability': 0.75, 'Willingness': 7.5},
        "Above-average risk tolerance": {'Ability': 0.75, 'Willingness': 22.5},
    }
    quadrant_df = pd.DataFrame.from_dict(quadrants, orient='index')
    quadrant_df['Quadrant'] = quadrant_df.index

    fig = px.scatter(df, x='Ability', y='Willingness', color='Category',
                     range_x=[0, 1], range_y=[0, 30],
                     labels={'Ability': 'Normalized Ability to Bear Risk', 'Willingness': 'Willingness Score'},
                     title='Client Risk Tolerance Matrix')

    fig.add_vline(x=0.5, line_width=1, line_dash="dash", color="black")
    fig.add_hline(y=15, line_width=1, line_dash="dash", color="black")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("""
    **Understanding the Matrix**
    The Client Risk Tolerance Matrix visualizes the relationship between an investor's ability to bear risk and their willingness to take risks. The matrix is divided into four quadrants, each representing a different risk tolerance category. The user's risk profile is plotted as a point on the matrix, indicating their overall risk tolerance.

    - **Below-average risk tolerance**: Investors in this quadrant have a low ability and willingness to take risks.
    - **Resolution needed**: These investors have a mismatch between their ability and willingness to take risks. Further discussion and analysis are needed to determine the appropriate investment strategy.
    - **Above-average risk tolerance**: Investors in this quadrant have a high ability and willingness to take risks.
    """)

