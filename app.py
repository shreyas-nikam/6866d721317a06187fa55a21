
import streamlit as st

st.set_page_config(page_title="Interactive IPS & Risk Profiler", layout="wide")

st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("QuLab")
st.divider()

st.markdown("""
# Interactive IPS & Risk Profiler

This application provides an interactive platform to understand the core concepts behind an Investment Policy Statement (IPS), with a focus on client risk profiling and objective setting. It helps to distinguish an investor's willingness to take risk from their ability to bear risk.

**Key Objectives:**

-   Demystify IPS Components
-   Quantify Risk Tolerance
-   Distinguish Risk Components (Willingness vs. Ability)
-   Visualize Risk Profile
-   Define Risk Objectives

**Target Audience:**

-   Students learning portfolio management
-   Aspiring financial advisors
-   Individual investors

**Reference Document:**

This application is designed to complement the "Basics of Portfolio Planning and Construction" document.  Specific concepts and examples from that document are referenced throughout the application.

**Instructions:**

Use the navigation menu in the sidebar to explore the different sections of the application.  Input your financial information and risk preferences to generate your personalized risk profile.
""")

page = st.sidebar.selectbox(label="Navigation", options=["Risk Profiler", "About"])

if page == "Risk Profiler":
    from application_pages.page1 import run_page1
    run_page1()
elif page == "About":
    from application_pages.page2 import run_page2
    run_page2()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
