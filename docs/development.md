# PromptTrap Development Guide

This guide provides instructions for setting up your development environment, running tests, and contributing to the PromptTrap project.

## 1. Setting Up Your Development Environment

### Prerequisites

- **Python 3.11+**: Ensure you have Python 3.11 or a newer version installed.
- **Poetry**: PromptTrap uses [Poetry](https://python-poetry.org/) for dependency management. If you don't have it, install it using pip:
  ```bash
  pip install poetry
  ```
- **Docker**: Required for building and running the application in containers, and for local testing of the Docker setup.

### Steps

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-org/prompttrap.git
    cd prompttrap
    ```

2.  **Install Dependencies:**
    Navigate to the project root and install the dependencies using Poetry:
    ```bash
    poetry install
    ```
    This command will create a virtual environment and install all the project's dependencies (including development dependencies like `pytest`).

3.  **Configure Environment Variables:**
    Create a `.env` file in the project root by copying the example file:
    ```bash
    cp .env.example .env
    ```
    Open the `.env` file and populate it with your actual API keys and desired configuration settings. This is crucial for the application to function correctly and for tests to pass.

    ```ini
    # Example .env content
    PROMPTTRAP_HOST=0.0.0.0
    PROMPTTRAP_PORT=8000
    PROMPTTRAP_LOG_LEVEL=INFO
    PROMPTTRAP_CORS_ORIGINS=*

    PROMPTTRAP_API_KEYS=your_secret_prompttrap_key_1,your_secret_prompttrap_key_2

    OPENAI_API_KEY=sk-your-openai-key
    OPENAI_BASE_URL=https://api.openai.com/v1
    CLAUDE_API_KEY=sk-ant-your-claude-key
    CLAUDE_BASE_URL=https://api.anthropic.com
    AZURE_OPENAI_API_KEY=your-azure-openai-key
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com

    REQUEST_TIMEOUT=30
    MAX_REQUEST_SIZE=10485760
    ```

4.  **Run the Application Locally:**
    You can run the FastAPI application using Uvicorn. The `--reload` flag is useful during development as it automatically reloads the server when code changes are detected.
    ```bash
    poetry run uvicorn core.main:app --host 0.0.0.0 --port 8000 --reload
    ```
    The API will be accessible at `http://localhost:8000`.

## 2. Running Tests

PromptTrap uses `pytest` for its unit and integration tests. All tests are located in the `tests/` directory.

To run all tests:

```bash
poetry run pytest
```

To run tests with verbose output:

```bash
poetry run pytest -v
```

To run a specific test file (e.g., `test_auth.py`):

```bash
poetry run pytest tests/test_auth.py
```

## 3. Code Quality and Linting

(Placeholder for future linters like Black, Flake8, MyPy)

## 4. Contributing Guidelines

(Placeholder for detailed contribution guidelines, e.g., branching strategy, pull request process, code review)

## 5. Project Structure

Refer to the `README.md` for an overview of the project's directory structure.
