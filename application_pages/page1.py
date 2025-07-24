
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
