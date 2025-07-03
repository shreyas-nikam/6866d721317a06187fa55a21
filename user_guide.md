id: 6866d721317a06187fa55a21_user_guide
summary: Portfolio Management User Guide
feedback link: https://docs.google.com/forms/d/e/1FAIpQLSfWkOK-in_bMMoHSZfcIvAeO58PAH9wrDqcxnJABHaxiDqhSA/viewform?usp=sf_link
environments: Web
status: Published
# Understanding Your Investment Risk Profile

## Introduction to Investment Risk Profiling
Duration: 05:00

Welcome to the Interactive IPS & Risk Profiler application! This tool is designed to help you understand fundamental concepts in personal finance, specifically focusing on Investment Policy Statements (IPS) and risk profiling.

An **Investment Policy Statement (IPS)** is a crucial document in investment management. It outlines an investor's objectives, constraints, and preferences, serving as a roadmap for managing their portfolio. A key part of developing an IPS is understanding the investor's **risk profile**.

Risk profiling involves assessing how much investment risk an individual is willing and able to take. This application focuses on distinguishing between two critical aspects of risk:

-   **Willingness to Take Risk:** This is a psychological or attitudinal factor. It reflects your personal comfort level with potential losses and market volatility. It's subjective and can be influenced by past experiences, personality traits, and beliefs about investing.
-   **Ability to Bear Risk:** This is an objective, financial factor. It's determined by your financial situation, such as your income, net worth, liabilities, and the length of your investment time horizon. Someone with a stable high income and a long time horizon generally has a greater ability to bear risk than someone with low income, high debt, and a short time horizon.

It is important to understand both aspects, as a mismatch between willingness and ability can lead to an inappropriate investment strategy.

This application will guide you through assessing these factors, calculating relevant scores, defining investment objectives, and visualizing your risk profile. It is designed to complement materials like the "Basics of Portfolio Planning and Construction" document by providing a hands-on way to explore these concepts.

The application uses simple formulas to help quantify these concepts:

- The **Ability Score** is calculated based on your financial inputs:
    $$ \text{Ability Score} = \frac{\text{Income}}{10000} + \frac{\text{Net Worth}}{50000} - \frac{\text{Liabilities}}{20000} + \frac{\text{Time Horizon}}{10} $$
- This score is then **Normalized** to fit a specific scale for visualization:
    $$ \text{Ability Score Normalized} = \frac{\text{Ability Score} - \text{Min\_Conceptual\_Ability\_Score}}{\text{Max\_Conceptual\_Ability\_Score} - \text{Min\_Conceptual\_Ability\_Score}} $$
    (where Min\_Conceptual\_Ability\_Score and Max\_Conceptual\_Ability\_Score are predefined reference points)
- The **Willingness Score** is calculated by summing up your responses to the psychometric questions, with some questions potentially inverted to ensure a higher score consistently means higher willingness:
    $$ \text{Willingness Score} = \sum_{i=1}^{5} \text{Psychometric Question Score}\_i $$

<aside class="positive">
Take your time in this section to understand the core ideas of risk profiling – the difference between <b>willingness</b> and <b>ability</b> is fundamental!
</aside>

## Exploring the Risk Profiler - Inputting Your Profile
Duration: 07:00

Now that you understand the basics, let's navigate to the Risk Profiler section of the application.

On the left-hand side of the application window, you will find a sidebar. Under "Navigation", ensure that "Risk Profiler" is selected.

The main area of the application will then display the "Risk Profiler" page. This page is divided into several sections, allowing you to input information about your financial situation and your attitude towards risk.

### Financial Factors (Ability to Bear Risk)

Scroll down to the section titled "Financial Factors (Ability to Bear Risk)". Here, you will find several input fields:

-   **Annual Income ($):** Enter your gross annual income. A higher income generally means you can absorb potential investment losses more easily, indicating a higher *ability* to bear risk.
-   **Net Worth ($):** Enter your net worth (total assets minus total liabilities). A higher net worth provides a larger financial cushion, increasing your *ability* to bear risk.
-   **Total Liabilities ($):** Enter your total outstanding debts. Higher liabilities can reduce your financial flexibility, potentially lowering your *ability* to bear risk.
-   **Investment Time Horizon (Years):** Use the slider to select how many years you plan to invest your money. A longer time horizon allows more time to recover from market downturns, increasing your *ability* to bear risk.
-   **Number of Dependents:** Use the slider to indicate the number of people who financially depend on you. More dependents can increase financial obligations, potentially reducing your *ability* to bear risk.
-   **Income Stability:** Select from the dropdown whether your income is Stable, Fluctuating, or Variable. Stable income provides more financial predictability, increasing your *ability* to bear risk.

Input your own financial details (or hypothetical values if you prefer). Observe how changing these values might intuitively affect your perceived ability to take risk.

### Psychometric Factors (Willingness to Take Risk)

Scroll further down to the section titled "Psychometric Factors (Willingness to Take Risk)". This section contains a series of slider questions designed to gauge your psychological comfort with investment risk:

-   Each question presents a statement related to investing or risk-taking.
-   You will use the slider to indicate your level of agreement or disagreement on a scale from 1 to 5. Pay attention to the labels (e.g., 1=Strongly Agree, 5=Strongly Disagree) for each specific question.

Answer these questions honestly based on your personal feelings and attitudes towards investing. Your responses here will contribute to your **Willingness Score**.

<aside class="positive">
Experiment with different values in the input fields. See how changing your income or time horizon affects the results later on. Similarly, try different responses to the psychometric questions to understand how they reflect varying levels of risk willingness.
</aside>

## Understanding Your Risk Profile - Scores and Categories
Duration: 06:00

After you have entered all your information in the previous step, the application automatically performs calculations based on the formulas mentioned in the introduction. Scroll down to the section titled "Calculated Scores".

Here, you will see the results:

-   **Ability Score:** This is the raw score calculated from your financial inputs using the first formula. It provides a numerical representation of your financial capacity to bear risk.
-   **Normalized Ability Score:** This score is the result of scaling the raw Ability Score to a range, typically between 0 and 1, using the normalization formula. This makes it easier to compare and plot on a standardized scale.
-   **Willingness Score:** This is the sum derived from your responses to the psychometric questions. A higher Willingness Score indicates a greater psychological comfort with risk.
-   **Overall Risk Tolerance Category:** Based on your Normalized Ability Score and Willingness Score, the application assigns you to one of three general risk tolerance categories:
    -   **Below-average risk tolerance:** Indicates both low ability and low willingness to take risk.
    -   **Above-average risk tolerance:** Indicates both high ability and high willingness to take risk.
    -   **Resolution needed:** Indicates a potential mismatch between your ability and willingness (e.g., high ability but low willingness, or low ability but high willingness). This category suggests that further discussion with a financial advisor might be necessary to reconcile these differences and determine an appropriate investment strategy.

Look at your calculated scores and assigned category. Do they align with how you perceive your own risk tolerance?

<aside class="positive">
The "Resolution needed" category is not a problem, but a prompt for deeper thought. If you land here, consider *why* there's a mismatch between your financial ability and your psychological comfort level.
</aside>

## Defining Risk Objectives and Visualizing Your Profile
Duration: 08:00

Continuing down the page, you will find sections for defining your investment objectives and visualizing your risk profile.

### Risk Objective Definition

This section allows you to express your risk preferences in more concrete terms related to potential investment outcomes:

-   **Maximum Acceptable Capital Loss (%):** Enter the maximum percentage of your investment capital that you are willing to lose over a specific period (e.g., in a single year or during a market downturn). This is an example of an **absolute risk objective**.
-   **Desired Benchmark Outperformance (%):** Enter the percentage by which you would like your investments to outperform a chosen market benchmark (e.g., the S&P 500). This is an example of a **relative risk objective**.

These objectives help translate your general risk tolerance into specific targets and constraints for portfolio management.

### Client Risk Tolerance Matrix

Finally, the application presents a visual representation of your risk profile in the form of a scatter plot titled "Client Risk Tolerance Matrix".

-   The **horizontal axis** represents your **Normalized Ability to Bear Risk**. It ranges from 0 to 1, with higher values indicating greater financial ability.
-   The **vertical axis** represents your **Willingness Score**. It ranges from 0 to 30 (or similar, depending on the scaling), with higher values indicating greater psychological willingness.
-   The matrix is divided into quadrants by dashed lines, typically separating the space at the midpoint of each axis (e.g., Normalized Ability = 0.5, Willingness Score = 15). These quadrants roughly correspond to the risk tolerance categories.
-   Your specific risk profile (based on your input) is plotted as a single point on this matrix. The color of the point corresponds to your assigned Overall Risk Tolerance Category.

**Understanding the Matrix:**

-   Points in the bottom-left quadrant generally represent **Below-average risk tolerance** (low ability, low willingness).
-   Points in the top-right quadrant generally represent **Above-average risk tolerance** (high ability, high willingness).
-   Points in the other two quadrants represent situations where **Resolution is needed** (e.g., high ability but low willingness, or low ability but high willingness).

The matrix provides a clear visual summary of where you stand regarding both components of risk tolerance.

<aside class="positive">
Look at where your point falls on the matrix. Does its position visually reinforce the Overall Risk Tolerance Category you were assigned? How does changing your input values (in Step 2) move the point on the graph?
</aside>

## Conclusion and Disclaimer
Duration: 02:00

You have now successfully used the Interactive IPS & Risk Profiler to assess your risk tolerance based on financial and psychological factors, define investment objectives, and visualize your risk profile on a matrix.

This application has demonstrated the key concepts of:

-   Understanding the components of an Investment Policy Statement (IPS).
-   Distinguishing between your Ability to Bear Risk (financial) and your Willingness to Take Risk (psychological).
-   Seeing how different factors contribute to these aspects of risk tolerance.
-   Translating general risk tolerance into specific risk objectives.
-   Visualizing the relationship between ability and willingness on a matrix.

Remember that this application is an educational tool. The calculations and categories provided are illustrative and based on simplified models.

<aside class="negative">
<b>Disclaimer:</b> This application is for educational purposes only and should not be considered financial advice. Investment decisions should always be made in consultation with a qualified financial advisor who can consider your complete financial situation and goals. The outputs of this tool are not recommendations for specific investments or strategies.
</aside>

Thank you for exploring the Interactive IPS & Risk Profiler! We hope this has provided a helpful introduction to the important concepts of investment risk profiling.
