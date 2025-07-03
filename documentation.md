id: 6866d721317a06187fa55a21_documentation
summary: Portfolio Management Documentation
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Building an Interactive Investment Risk Profiler with Streamlit

## Introduction and Setup
Duration: 0:10:00

Welcome to the "Building an Interactive Investment Risk Profiler with Streamlit" codelab!

In the world of finance and investment management, understanding a client's risk tolerance is paramount. It's the foundation upon which suitable investment strategies and portfolios are built. A key document in this process is the **Investment Policy Statement (IPS)**, which outlines the client's objectives, constraints, and risk profile.

This application provides an **interactive platform** to explore these concepts, focusing specifically on **client risk profiling** and **objective setting**. A critical distinction highlighted is that between an investor's **willingness** to take risk (a psychological factor) and their **ability** to bear risk (a financial factor). By using this application, you will learn how to quantify these different facets of risk and visualize their relationship.

**Key Concepts Covered:**

*   **Investment Policy Statement (IPS):** Understanding its components, particularly risk objectives.
*   **Risk Tolerance:** Demystifying the concept and its importance.
*   **Willingness vs. Ability:** Differentiating between the psychological and financial aspects of risk.
*   **Risk Quantification:** Learning how financial and psychometric factors can be used to calculate risk scores.
*   **Visualization:** Using a Risk Tolerance Matrix to visually represent an investor's profile.
*   **Risk Objectives:** Defining absolute and relative risk targets.

This codelab guides you through the code of a Streamlit application that implements these concepts.

**Reference Document:**

The application is designed to complement foundational material on portfolio planning, such as sections found in "Basics of Portfolio Planning and Construction."

**Prerequisites:**

*   Basic understanding of Python.
*   Familiarity with financial concepts like income, net worth, liabilities, and investment time horizon is helpful but not strictly necessary to follow the code.
*   [Optional] Basic familiarity with Streamlit.

**Setting up the Environment:**

1.  Ensure you have Python installed (version 3.7 or higher recommended).
2.  Install the necessary libraries: Streamlit, Plotly, and Pandas. Open your terminal or command prompt and run:

    ```console
    pip install streamlit plotly pandas
    ```
3.  Create a project directory (e.g., `risk_profiler_app`).
4.  Inside the project directory, create a file named `app.py`.
5.  Create a subdirectory named `application_pages`.
6.  Inside the `application_pages` directory, create a file named `risk_profiler.py`.

Now, copy the following code into the respective files:

**`app.py`:**

```python
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
```

**`application_pages/risk_profiler.py`:**

```python
import streamlit as st
import plotly.express as px
import pandas as pd

def run_risk_profiler():
    st.header("Risk Profiler")

    #  Ability to Bear Risk Questionnaire (Financial Factors) 
    st.subheader("Financial Factors (Ability to Bear Risk)")
    income = st.number_input('Annual Income ($)', value=50000)
    net_worth = st.number_input('Net Worth ($)', value=250000)
    liabilities = st.number_input('Total Liabilities ($)', value=50000)
    time_horizon = st.slider('Investment Time Horizon (Years)', min_value=1, max_value=30, value=10)
    dependents = st.slider('Number of Dependents', min_value=0, max_value=5, value=2)
    income_stability = st.selectbox('Income Stability', ['Stable', 'Fluctuating', 'Variable'])

    #  Willingness to Take Risk Assessment (Psychometric Factors) 
    st.subheader("Psychometric Factors (Willingness to Take Risk)")
    q1 = st.slider('Question 1: "Investing is too difficult to understand." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q2 = st.slider('Question 2: "I get anxious when the market fluctuates." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q3 = st.slider('Question 3: "I prefer investments with guaranteed returns, even if the returns are lower." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q4 = st.slider('Question 4: "I am comfortable with the possibility of losing money on my investments." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)
    q5 = st.slider('Question 5: "I like to take risks in other areas of my life." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)

    #  Calculations 
    ability_score = (income / 10000) + (net_worth / 50000) - (liabilities / 20000) + (time_horizon / 10)
    min_conceptual_ability_score = -5  # Example minimum value
    max_conceptual_ability_score = 20 # Example maximum value

    ability_score_normalized = (ability_score - min_conceptual_ability_score) / (max_conceptual_ability_score - min_conceptual_ability_score)
    willingness_score = (6 - q1) + (6 - q2) + (6 - q3) + q4 + q5 # Inverting the first three questions so that higher score is higher willingness

    #  Risk Tolerance Category 
    if ability_score_normalized < 0.5 and willingness_score < 15:
        risk_tolerance_category = "Below-average risk tolerance"
    elif ability_score_normalized >= 0.5 and willingness_score >= 15:
        risk_tolerance_category = "Above-average risk tolerance"
    else:
        risk_tolerance_category = "Resolution needed"

    #  Display Calculated Scores 
    st.subheader("Calculated Scores")
    st.markdown(f"Ability Score: {ability_score:.2f}")
    st.markdown(f"Normalized Ability Score: {ability_score_normalized:.2f}")
    st.markdown(f"Willingness Score: {willingness_score}")
    st.markdown(f"Overall Risk Tolerance Category: {risk_tolerance_category}")

    #  Risk Objective Definition 
    st.subheader("Risk Objective Definition")
    absolute_risk_objective = st.number_input('Maximum Acceptable Capital Loss (%)', min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    relative_risk_objective = st.number_input('Desired Benchmark Outperformance (%)', min_value=0.0, max_value=10.0, value=2.0, step=0.1)

    #  Visualization 
    st.subheader("Client Risk Tolerance Matrix")

    # Create a dataframe for the scatter plot
    data = {'Ability': [ability_score_normalized], 'Willingness': [willingness_score], 'Category': [risk_tolerance_category]}
    df = pd.DataFrame(data)

    # Define quadrants - Note: These are for text placement, the plot logic uses vline/hline
    # quadrants = {
    #     "Below-average risk tolerance": {'Ability': 0.25, 'Willingness': 7.5},
    #     "Resolution needed (Low Ability)": {'Ability': 0.25, 'Willingness': 22.5},
    #     "Resolution needed (High Ability)": {'Ability': 0.75, 'Willingness': 7.5},
    #     "Above-average risk tolerance": {'Ability': 0.75, 'Willingness': 22.5},
    # }
    # quadrant_df = pd.DataFrame.from_dict(quadrants, orient='index')
    # quadrant_df['Quadrant'] = quadrant_df.index

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
```

Once you have created these files and pasted the code, your project structure should look like this:

```
risk_profiler_app/
├── app.py
└── application_pages/
    └── risk_profiler.py
```

You are now ready to explore the application's code and functionality.

## The Main Application (`app.py`)
Duration: 0:05:00

The `app.py` file serves as the main entry point and layout manager for the Streamlit application.

Let's break down its components:

*   **Import Streamlit:** `import streamlit as st` is the standard way to import the library.
*   **Page Configuration:** `st.set_page_config(...)` sets the browser tab title and the layout style (`wide` makes the main content area wider).
*   **Sidebar Elements:**
    *   `st.sidebar.image(...)`: Adds an image (QuantUniversity logo) to the sidebar.
    *   `st.sidebar.divider()`: Adds a visual separator.
    *   `st.title(...)`: Sets the main title of the application in the main content area.
    *   `st.divider()`: Adds another visual separator in the main content area.
*   **Introduction Markdown:** A large block of `st.markdown("""...""")` is used to provide an overview of the application, its objectives, explain the concept of risk tolerance (Willingness vs. Ability), list the formulas used for calculations, and mention the reference document.
    *   Notice the use of Markdown for formatting (bold text, lists) and $\$\$...$\$\$$ for rendering mathematical formulas using LaTeX syntax.
*   **Sidebar Navigation:** `st.sidebar.selectbox(...)` creates a dropdown menu in the sidebar labeled "Navigation". In this version, the only option available is "Risk Profiler".
*   **Page Routing Logic:**
    ```python
    page = st.sidebar.selectbox(label="Navigation", options=["Risk Profiler"])

    if page == "Risk Profiler":
        from application_pages.risk_profiler import run_risk_profiler
        run_risk_profiler()
    ```
    This block checks the selected value from the navigation dropdown. If "Risk Profiler" is selected, it dynamically imports the `run_risk_profiler` function from the `application_pages.risk_profiler` module and executes it. This is how Streamlit applications handle multi-page layouts by conditionally rendering content based on user selection.
*   **Footer Information:** The application concludes with another divider, copyright information (`st.write`), and a disclaimer (`st.caption`).

This file sets the stage, provides essential context and formulas, and manages which part of the application (currently just the Risk Profiler) is displayed based on user interaction with the sidebar.

## The Risk Profiler Module (`risk_profiler.py`)
Duration: 0:15:00

The `application_pages/risk_profiler.py` file contains the core logic and user interface for the interactive risk assessment. All its functionality is encapsulated within the `run_risk_profiler()` function, which is called by `app.py`.

Let's walk through the sections within `run_risk_profiler()`:

*   **Page Header:** `st.header("Risk Profiler")` sets the main header for this section of the application.
*   **Financial Factors (Ability to Bear Risk):**
    ```python
    st.subheader("Financial Factors (Ability to Bear Risk)")
    income = st.number_input('Annual Income ($)', value=50000)
    net_worth = st.number_input('Net Worth ($)', value=250000)
    liabilities = st.number_input('Total Liabilities ($)', value=50000)
    time_horizon = st.slider('Investment Time Horizon (Years)', min_value=1, max_value=30, value=10)
    dependents = st.slider('Number of Dependents', min_value=0, max_value=5, value=2)
    income_stability = st.selectbox('Income Stability', ['Stable', 'Fluctuating', 'Variable'])
    ```
    This section uses various Streamlit input widgets to collect financial data from the user.
    *   `st.subheader`: Creates a subheading.
    *   `st.number_input`: Allows users to enter numerical values (e.g., income, net worth, liabilities). Default values are provided.
    *   `st.slider`: Provides a slider for selecting a value within a specified range (e.g., time horizon, number of dependents).
    *   `st.selectbox`: Creates a dropdown menu for selecting one option from a list (e.g., income stability).

    <aside class="positive">
    Notice how Streamlit widgets like `st.number_input` and `st.slider` automatically handle data type conversion (to float or int) and provide a user-friendly interface for inputting financial data.
    </aside>

*   **Psychometric Factors (Willingness to Take Risk):**
    ```python
    st.subheader("Psychometric Factors (Willingness to Take Risk)")
    q1 = st.slider('Question 1: "Investing is too difficult to understand." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q2 = st.slider('Question 2: "I get anxious when the market fluctuates." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q3 = st.slider('Question 3: "I prefer investments with guaranteed returns, even if the returns are lower." (1=Strongly Agree, 5=Strongly Disagree)', min_value=1, max_value=5, value=3)
    q4 = st.slider('Question 4: "I am comfortable with the possibility of losing money on my investments." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)
    q5 = st.slider('Question 5: "I like to take risks in other areas of my life." (1=Strongly Disagree, 5=Strongly Agree)', min_value=1, max_value=5, value=3)
    ```
    This section uses `st.slider` widgets to gather responses to psychometric questions designed to gauge the user's psychological comfort level with risk. The questions use a 5-point Likert scale.

    <aside class="negative">
    While dependents and income stability are collected under "Ability to Bear Risk", they are not used in the direct calculation of the `ability_score` in the provided code. This is a common simplification in educational examples but important to note. The core ability calculation relies on Income, Net Worth, Liabilities, and Time Horizon.
    </aside>

## Risk Score Calculations
Duration: 0:07:00

This section of the code performs the quantitative assessment of the user's risk profile based on the inputs from the previous step.

```python
#  Calculations 
ability_score = (income / 10000) + (net_worth / 50000) - (liabilities / 20000) + (time_horizon / 10)
min_conceptual_ability_score = -5  # Example minimum value
max_conceptual_ability_score = 20 # Example maximum value

ability_score_normalized = (ability_score - min_conceptual_ability_score) / (max_conceptual_ability_score - min_conceptual_ability_score)
willingness_score = (6 - q1) + (6 - q2) + (6 - q3) + q4 + q5 # Inverting the first three questions so that higher score is higher willingness
```

Let's break down these calculations:

1.  **Ability Score Calculation:**
    $$ \text{Ability Score} = \frac{\text{Income}}{10000} + \frac{\text{Net Worth}}{50000} - \frac{\text{Liabilities}}{20000} + \frac{\text{Time Horizon}}{10} $$
    *   This formula is a simplified representation of how financial factors *could* contribute to the ability to bear risk.
    *   Higher income, net worth, and time horizon positively contribute to the score.
    *   Higher liabilities negatively contribute to the score.
    *   The divisors (10000, 50000, 20000, 10) are scaling factors used to bring the different metrics into a comparable range for summation. These are arbitrary scaling factors chosen for this specific example.

2.  **Normalized Ability Score Calculation:**
    $$ \text{Ability Score Normalized} = \frac{\text{Ability Score} - \text{Min\_Conceptual\_Ability\_Score}}{\text{Max\_Conceptual\_Ability\_Score} - \text{Min\_Conceptual\_Ability\_Score}} $$
    *   The raw `ability_score` can vary significantly depending on the inputs. Normalizing it to a range, typically [0, 1], makes it easier to interpret and compare consistently, especially for plotting purposes.
    *   `min_conceptual_ability_score` and `max_conceptual_ability_score` are defined as example bounds for the theoretical range of the ability score. The normalization maps the calculated `ability_score` onto the [0, 1] range based on these bounds.
    *   *Self-correction*: While the formula is shown, the code *doesn't* explicitly clamp the normalized score to [0, 1] using `np.clip` or similar after the calculation in this version of the code. The Plotly express `range_x=[0, 1]` will handle the plot limits, but the displayed normalized score might theoretically fall outside [0, 1] if the calculated `ability_score` falls outside the `min_conceptual_ability_score` to `max_conceptual_ability_score` range.

3.  **Willingness Score Calculation:**
    $$ \text{Willingness Score} = (6 - Q_1) + (6 - Q_2) + (6 - Q_3) + Q_4 + Q_5 $$
    *   This score is derived from the user's responses to the five psychometric questions.
    *   For questions 1, 2, and 3 (where agreement indicates *lower* willingness), the score is inverted by subtracting the response from 6 (since the scale is 1-5, 6-1=5, 6-5=1). This ensures that a higher score on these questions (disagreeing) contributes *positively* to the willingness score, aligning with questions 4 and 5 where agreement indicates *higher* willingness.
    *   For questions 4 and 5 (where agreement indicates *higher* willingness), the score is simply the user's response.
    *   The scores from all five questions (with the first three inverted) are summed to get the total `willingness_score`. The possible range for this score is $5 \times 1 = 5$ (lowest willingness) to $5 \times 5 = 25$ (highest willingness).

After these calculations, the application proceeds to determine the risk tolerance category and display the results.

## Determining the Risk Tolerance Category
Duration: 0:03:00

Based on the calculated normalized ability score and the willingness score, the application categorizes the user's overall risk tolerance.

```python
#  Risk Tolerance Category 
if ability_score_normalized < 0.5 and willingness_score < 15:
    risk_tolerance_category = "Below-average risk tolerance"
elif ability_score_normalized >= 0.5 and willingness_score >= 15:
    risk_tolerance_category = "Above-average risk tolerance"
else:
    risk_tolerance_category = "Resolution needed"
```

This simple conditional logic divides the risk matrix into four conceptual areas:

*   If normalized ability is below 0.5 **AND** willingness score is below 15: The category is "Below-average risk tolerance". This corresponds to the bottom-left quadrant of the risk matrix, where both financial capacity and psychological comfort for risk are low.
*   If normalized ability is 0.5 or above **AND** willingness score is 15 or above: The category is "Above-average risk tolerance". This corresponds to the top-right quadrant, where both financial capacity and psychological comfort for risk are high.
*   In all other cases: The category is "Resolution needed". This captures the two "mismatch" quadrants:
    *   High ability, low willingness (Top-left).
    *   Low ability, high willingness (Bottom-right).

<aside class="positive">
The "Resolution needed" category is crucial in real-world financial planning. It signifies a potential conflict between what an investor *can* afford to lose and what they are *comfortable* losing. This mismatch requires further discussion and guidance from a financial advisor to align expectations and strategy.
</aside>

## Displaying Calculated Scores
Duration: 0:03:00

Once the scores and category are determined, the application displays them to the user using `st.markdown`.

```python
#  Display Calculated Scores 
st.subheader("Calculated Scores")
st.markdown(f"Ability Score: {ability_score:.2f}")
st.markdown(f"Normalized Ability Score: {ability_score_normalized:.2f}")
st.markdown(f"Willingness Score: {willingness_score}")
st.markdown(f"Overall Risk Tolerance Category: {risk_tolerance_category}")
```

*   `st.subheader("Calculated Scores")` adds a clear heading for this section.
*   `st.markdown(f"...")` is used to display the results. The f-string formatting is used to embed the calculated Python variables directly into the markdown text.
*   `{ability_score:.2f}` formats the ability score to two decimal places for readability.

This provides immediate feedback to the user on the results of their inputs and the subsequent calculations.

## Defining Risk Objectives
Duration: 0:04:00

An important part of an Investment Policy Statement (IPS) is defining specific investment objectives and constraints, including risk objectives. This section allows the user to specify quantitative risk goals.

```python
#  Risk Objective Definition 
st.subheader("Risk Objective Definition")
absolute_risk_objective = st.number_input('Maximum Acceptable Capital Loss (%)', min_value=0.0, max_value=100.0, value=5.0, step=0.1)
relative_risk_objective = st.number_input('Desired Benchmark Outperformance (%)', min_value=0.0, max_value=10.0, value=2.0, step=0.1)
```

*   `st.subheader("Risk Objective Definition")` introduces this section.
*   Two `st.number_input` widgets are used:
    *   `Maximum Acceptable Capital Loss (%)`: This represents an **absolute** risk objective – defining the maximum percentage drop from peak value or initial capital the investor is willing to tolerate. It has a range of 0% to 100%.
    *   `Desired Benchmark Outperformance (%)`: This represents a **relative** risk objective – defining how much better the investor wants their portfolio to perform compared to a specific benchmark index (e.g., S&P 500). It has a range of 0% to 10%.

While these objectives are collected, the current application does not use them in the risk scoring or visualization. In a more advanced application, these objectives would guide portfolio construction and allocation strategies, potentially influencing or being influenced by the calculated risk tolerance.

## Visualizing the Risk Profile
Duration: 0:10:00

The final section of the Risk Profiler visualizes the calculated risk profile on a matrix. This is a powerful way to understand where the user stands in terms of their combined ability and willingness to take risk.

```python
#  Visualization 
st.subheader("Client Risk Tolerance Matrix")

# Create a dataframe for the scatter plot
data = {'Ability': [ability_score_normalized], 'Willingness': [willingness_score], 'Category': [risk_tolerance_category]}
df = pd.DataFrame(data)

fig = px.scatter(df, x='Ability', y='Willingness', color='Category',
                 range_x=[0, 1], range_y=[0, 30], # Adjusted range for Willingness score (5-25 possible)
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
```

*   `st.subheader("Client Risk Tolerance Matrix")` sets the heading for the visualization.
*   **Data Preparation:** A Pandas DataFrame (`df`) is created with a single row containing the calculated `ability_score_normalized`, `willingness_score`, and `risk_tolerance_category`. Plotly Express works well with DataFrames.
*   **Creating the Scatter Plot:** `plotly.express as px` is used to generate the scatter plot.
    *   `px.scatter()` takes the DataFrame (`df`), specifies 'Ability' for the x-axis and 'Willingness' for the y-axis.
    *   `color='Category'` instructs Plotly to color the single data point based on the `risk_tolerance_category`.
    *   `range_x=[0, 1]` sets the x-axis limits from 0 to 1 (corresponding to the normalized ability score).
    *   `range_y=[0, 30]` sets the y-axis limits. A range of 0-30 comfortably contains the possible willingness scores (5-25).
    *   `labels` provide friendly names for the axes.
    *   `title` sets the plot title.
*   **Adding Quadrant Lines:**
    *   `fig.add_vline(x=0.5, ...)` adds a vertical dashed black line at x=0.5, visually separating the low and high ability ranges.
    *   `fig.add_hline(y=15, ...)` adds a horizontal dashed black line at y=15, visually separating the low and high willingness ranges.
    These lines divide the matrix into the four quadrants discussed earlier.
*   **Displaying the Plot:** `st.plotly_chart(fig, use_container_width=True)` renders the interactive Plotly figure in the Streamlit application, making it fill the available width.
*   **Matrix Explanation:** A final `st.markdown` block provides a textual explanation of the matrix and what each quadrant represents, reinforcing the visual information.

This visualization is the culmination of the risk profiling process, providing a clear graphical summary of the user's risk profile.

## Running and Interacting with the Application
Duration: 0:05:00

You have now set up the application and reviewed its code structure and logic. It's time to run it and see it in action!

1.  Open your terminal or command prompt.
2.  Navigate to the root directory of your project (the one containing `app.py`).
    ```console
    cd path/to/your/risk_profiler_app
    ```
3.  Run the Streamlit application using the command:
    ```console
    streamlit run app.py
    ```
4.  Your web browser should automatically open a new tab displaying the application. If not, open your browser and go to `http://localhost:8501`.

**Interacting:**

*   Explore the introductory text and formulas on the main page.
*   Use the sidebar navigation dropdown (currently only "Risk Profiler") to ensure you are on the Risk Profiler page.
*   Interact with the input widgets in the "Financial Factors" and "Psychometric Factors" sections. Change the values for income, net worth, time horizon, and the responses to the questions.
*   As you change the inputs, observe how the "Calculated Scores" section updates in real-time.
*   Pay close attention to how the point on the "Client Risk Tolerance Matrix" plot moves based on your inputs. See how it transitions between the different quadrants ("Below-average risk tolerance", "Resolution needed", "Above-average risk tolerance").
*   Try to input values that place you in each of the four conceptual quadrants to understand the effect of both high/low ability and high/low willingness.
*   Experiment with the "Risk Objective Definition" inputs, although note that they don't currently affect the score calculations or the plot.

<aside class="positive">
Streamlit's automatic re-running of the script whenever input widgets change is what makes the application interactive and provides instant feedback on how different inputs affect the risk profile.
</aside>

You have now successfully set up, explored, and interacted with the Investment Risk Profiler application. You should have a better understanding of how financial and psychological factors can be used to quantify and visualize client risk tolerance within the context of investment planning.
