
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we explore the fundamentals of portfolio management with a focus on risk assessment and Investment Policy Statements (IPS). This application helps you understand your risk profile by considering both your ability and willingness to take risk.

The application consists of three main pages:

-   **Risk Profiler**: Input your financial details and psychological risk attitudes to assess your overall risk tolerance.
-   **Investment Objectives**: Define your investment objectives, including absolute and relative risk targets.
-   **Portfolio Allocation**: Explore different asset allocation strategies based on your risk profile and investment objectives.

For more information on the concepts discussed in this lab, refer to the "Basics of Portfolio Planning and Construction" document.
""")

page = st.sidebar.selectbox(label="Navigation", options=["Risk Profiler", "Investment Objectives", "Portfolio Allocation"])
if page == "Risk Profiler":
    from application_pages.risk_profiler import run_risk_profiler
    run_risk_profiler()
elif page == "Investment Objectives":
    from application_pages.investment_objectives import run_investment_objectives
    run_investment_objectives()
elif page == "Portfolio Allocation":
    from application_pages.portfolio_allocation import run_portfolio_allocation
    run_portfolio_allocation()
