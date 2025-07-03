
import streamlit as st

st.set_page_config(page_title="Interactive IPS & Risk Profiler", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Interactive IPS & Risk Profiler")
st.divider()
st.markdown("""
This application provides an intuitive and interactive platform for understanding the core concepts behind an Investment Policy Statement (IPS), focusing on client risk profiling and objective setting. It relates to the "Basics of Portfolio Planning and Construction" document.

**Key Objectives:**
- Demystify IPS Components.
- Quantify Risk Tolerance.
- Distinguish Risk Components: Willingness vs. Ability to take risk.
- Visualize Risk Profile.
- Define Risk Objectives.
- Interactive Learning.

**Understanding Risk Tolerance**

Risk tolerance is a crucial aspect of investment planning. It involves understanding an investor's willingness and ability to take risks.

- **Willingness to Take Risk:** This is a subjective, psychological factor reflecting an investor's comfort level with potential losses.  It's influenced by personality, past experiences, and perception of risk.

- **Ability to Bear Risk:** This is an objective factor based on financial circumstances, such as income, net worth, time horizon, and liabilities.

The interplay between these two factors determines an investor's overall risk tolerance and shapes their investment strategy.

The application uses the following formulae:

- Ability Score:
    $$ \text{Ability Score} = \frac{\text{Income}}{10000} + \frac{\text{Net Worth}}{50000} - \frac{\text{Liabilities}}{20000} + \frac{\text{Time Horizon}}{10} $$

- Normalized Ability Score:
    $$ \text{Ability Score Normalized} = \frac{\text{Ability Score} - \text{Min\_Conceptual\_Ability\_Score}}{\text{Max\_Conceptual\_Ability\_Score} - \text{Min\_Conceptual\_Ability\_Score}} $$

- Willingness Score:
    $$ \text{Willingness Score} = \sum_{i=1}^{5} \text{Psychometric Question Score}\_i $$
""")

page = st.sidebar.selectbox(label="Navigation", options=["Risk Profiler"])

if page == "Risk Profiler":
    from application_pages.risk_profiler import run_risk_profiler
    run_risk_profiler()

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity. "
           "This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors")
