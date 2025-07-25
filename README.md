# PromptTrap: Zero-Trust AI Gateway

PromptTrap is a zero-trust AI gateway designed to act as a model-agnostic proxy for various Large Language Model (LLM) APIs, including OpenAI, Anthropic Claude, and Azure OpenAI.

This project is currently in **Phase 1** of its MVP development, focusing on establishing the foundational infrastructure and core proxy functionality for intercepting, authenticating, and forwarding LLM API requests.

## Features (Phase 1)

- **API Key Authentication**: Secure access to the proxy via `Authorization: Bearer <token>` headers.
- **LLM API Proxying**: Routes requests to OpenAI, Anthropic Claude, and Azure OpenAI.
- **Health Checks**: `/health` and `/version` endpoints for monitoring.
- **Configuration**: Environment variable-based configuration for API keys, endpoints, and other settings.
- **Docker Support**: Containerized deployment using Docker.

## Project Structure

```
prompttrap/
├── README.md
├── LICENSE (Apache 2.0)
├── .gitignore
├── pyproject.toml
├── docker-compose.yml
├── .env.example
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── security-scan.yml
├── core/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entry point
│   ├── config.py            # Configuration management
│   ├── auth.py              # Authentication middleware
│   ├── proxy/
│   │   ├── __init__.py
│   │   ├── router.py        # Main proxy routing logic
│   │   ├── openai.py        # OpenAI-specific handling
│   │   ├── claude.py        # Claude-specific handling
│   │   └── azure.py         # Azure OpenAI handling
│   └── health.py            # Health check endpoints
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Pytest configuration
│   ├── test_auth.py
│   ├── test_proxy.py
│   ├── test_health.py
│   └── integration/
│       ├── __init__.py
│       └── test_e2e.py
└── docs/
    ├── api.md
    ├── development.md
    └── deployment.md
```

## Local Development Setup

### Prerequisites

- Python 3.11+
- Poetry (for dependency management)
- Docker (for containerized development and deployment)

### 1. Clone the repository

```bash
git clone https://github.com/your-org/prompttrap.git
cd prompttrap
```

### 2. Install Dependencies

PromptTrap uses [Poetry](https://python-poetry.org/) for dependency management. If you don't have Poetry installed, you can install it via pip:

```bash
pip install poetry
```

Then, install the project dependencies:

```bash
poetry install
```

### 3. Configure Environment Variables

Copy the example environment file and fill in your API keys and other settings:

```bash
cp .env.example .env
```

Edit the `.env` file with your actual API keys and desired configurations. For example:

```ini
PROMPTTRAP_API_KEYS=your_secret_prompttrap_key
OPENAI_API_KEY=sk-your-openai-key
CLAUDE_API_KEY=sk-ant-your-claude-key
AZURE_OPENAI_API_KEY=your-azure-openai-key
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com
```

### 4. Run the Application Locally

To start the FastAPI application using Uvicorn:

```bash
poetry run uvicorn core.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be accessible at `http://localhost:8000`.

### 5. Running Tests

To run the unit and integration tests:

```bash
poetry run pytest
```

## Docker Deployment

### 1. Build the Docker Image

```bash
docker-compose build
```

### 2. Run the Docker Container

Ensure your `.env` file is configured correctly, then:

```bash
docker-compose up
```

The application will be running in a Docker container, accessible via `http://localhost:8000`.

## API Endpoints

- `/health`: Health check endpoint.
- `/version`: Returns service version information.
- `/api/openai/{path:path}`: Proxies requests to the OpenAI API.
- `/api/claude/{path:path}`: Proxies requests to the Anthropic Claude API.
- `/api/azureopenai/{path:path}`: Proxies requests to the Azure OpenAI API.

For detailed API documentation, refer to `docs/api.md`.

## Contributing

Contributions are welcome! Please refer to `docs/development.md` for guidelines on setting up your development environment and contributing to the project.

## Licensing

- Core: [Apache 2.0 License](./LICENSE)
- Enterprise Features (e.g., policy engine, SSO, dashboard): [Enterprise License](./LICENSE-ENTERPRISE.txt)