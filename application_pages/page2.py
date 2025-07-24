
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
    else:
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
