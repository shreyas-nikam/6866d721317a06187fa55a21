
import streamlit as st
st.set_page_config(page_title="QuLab", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()
st.markdown("""
In this lab, we explore the fundamentals of portfolio management with a focus on risk assessment and Investment Policy Statements (IPS). This interactive application allows you to understand your own risk profile and how it influences investment decisions. The application implements concepts from the "Basics of Portfolio Planning and Construction" document, especially concerning risk tolerance (page 6).

Key features include:
- Interactive risk profiling based on financial and psychometric factors.
- Visualization of your risk tolerance category.
- Definition of absolute and relative risk objectives.
""")

page = st.sidebar.selectbox(label="Navigation", options=["Risk Profiler", "Asset Allocation", "Portfolio Optimization"])
if page == "Risk Profiler":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "Asset Allocation":
    from application_pages.page2 import run_page2
    run_page2()
elif page == "Portfolio Optimization":
    from application_pages.page3 import run_page3
    run_page3()
