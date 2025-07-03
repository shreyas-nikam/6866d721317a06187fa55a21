
# Interactive IPS & Risk Profiler

This Streamlit application provides an interactive tool for understanding Investment Policy Statements (IPS) and risk profiling.

## Prerequisites

- Docker (optional, for containerized deployment)
- Python 3.9 or higher

## Installation

1.  Clone the repository.
2.  Create a virtual environment (optional):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```
3.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

1.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

## Running with Docker

1.  Build the Docker image:
    ```bash
    docker build -t interactive-ips .
    ```
2.  Run the Docker container:
    ```bash
    docker run -p 8501:8501 interactive-ips
    ```

The application will be accessible at `http://localhost:8501`.
