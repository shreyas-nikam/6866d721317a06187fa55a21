# Interactive IPS & Risk Profiler

![Streamlit App](https://static.streamlit.io/examples/badge.svg)
![QuantUniversity Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

This application provides an intuitive and interactive platform for understanding the core concepts behind an Investment Policy Statement (IPS), focusing specifically on client risk profiling and objective setting. Designed as an educational lab project, it helps users explore the critical distinction between an investor's **willingness** to take risk and their **ability** to bear risk, and how these factors combine to determine an overall risk profile.

The application is built to complement foundational knowledge in portfolio management, particularly concepts found in documents like "Basics of Portfolio Planning and Construction."

## Key Objectives

*   **Demystify IPS Components:** Understand the initial steps of defining investor characteristics and objectives.
*   **Quantify Risk Tolerance:** Assess risk tolerance through interactive inputs for both financial and psychological factors.
*   **Distinguish Risk Components:** Clearly differentiate between an investor's objective ability to bear risk (based on financial situation) and their subjective willingness to take risk (based on psychological preferences).
*   **Visualize Risk Profile:** See where your calculated risk profile lands on a matrix that plots ability vs. willingness.
*   **Define Risk Objectives:** Practice setting quantitative risk objectives (absolute loss limits, relative performance goals).
*   **Interactive Learning:** Engage directly with the concepts through a user-friendly interface.

## Features

*   **Financial Factor Input:** Collects data on income, net worth, liabilities, time horizon, dependents, and income stability to assess Ability to Bear Risk.
*   **Psychometric Assessment:** Uses a series of interactive slider questions to gauge Willingness to Take Risk.
*   **Score Calculation:** Automatically calculates and displays:
    *   Ability Score (based on financial inputs)
    *   Normalized Ability Score (scaled between 0 and 1)
    *   Willingness Score (based on psychometric responses)
*   **Risk Categorization:** Assigns an overall Risk Tolerance Category (e.g., Below-average, Above-average, Resolution needed) based on combined scores.
*   **Risk Objective Input:** Allows users to define specific absolute and relative risk targets.
*   **Interactive Visualization:** Plots the calculated risk profile on a Client Risk Tolerance Matrix using Plotly, providing a visual representation of the ability/willingness relationship.
*   **Educational Context:** Provides explanations and context for the inputs, calculations, and visualizations.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for educational purposes.

### Prerequisites

You will need to have Python installed on your system. This project is compatible with Python 3.7+.

```bash
# Check if Python is installed
python --version
# Check if pip is installed
pip --version
```

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```
    *(Replace `<repository_url>` and `<repository_directory>` with the actual URL and directory name)*

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```
    *   On Windows:
        ```bash
        .venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

3.  **Install dependencies:**
    Create a `requirements.txt` file in the root directory of the project with the following content:
    ```txt
    streamlit
    plotly
    pandas
    ```
    Then install the packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Navigate to the project directory:**
    ```bash
    cd <repository_directory>
    ```

2.  **Run the Streamlit application:**
    ```bash
    streamlit run app.py
    ```

3.  The application will open in your default web browser. Use the interactive elements (number inputs, sliders, selectboxes) on the "Risk Profiler" page to input your financial information and risk preferences. The application will automatically calculate and display your scores and plot your risk profile on the matrix.

## Project Structure

```
.
├── app.py
└── application_pages/
    └── risk_profiler.py
├── requirements.txt  (created during installation)
```

*   `app.py`: The main entry point for the Streamlit application. Handles page setup, sidebar navigation, and loading page modules.
*   `application_pages/`: A directory containing the code for different sections (pages) of the application.
*   `application_pages/risk_profiler.py`: Contains the Streamlit code specifically for the Interactive Risk Profiler page, including inputs, calculations, visualizations, and explanations.

## Technology Stack

*   **Framework:** Streamlit
*   **Programming Language:** Python
*   **Data Manipulation:** Pandas
*   **Visualization:** Plotly

## Contributing

This project is primarily designed as an educational lab. Contributions are generally not accepted in the form of pull requests on the main lab repository, but feel free to fork the repository and experiment with your own modifications or improvements.

## License

© 2025 QuantUniversity. All Rights Reserved.

The purpose of this demonstration is solely for educational use and illustration. Any reproduction of this demonstration requires prior written consent from QuantUniversity.

This lab was generated using the QuCreate platform. QuCreate relies on AI models for generating code, which may contain inaccuracies or errors.

## Contact

For inquiries related to this project or QuantUniversity, please visit [https://www.quantuniversity.com/](https://www.quantuniversity.com/).
