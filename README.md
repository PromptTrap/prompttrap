# PromptTrap: Zero-Trust AI Gateway

PromptTrap is a zero-trust AI gateway designed to act as a model-agnostic proxy for various Large Language Model (LLM) APIs, including OpenAI, Anthropic Claude, and Azure OpenAI.

This project is currently in **Phase 1** of its MVP development, focusing on establishing the foundational infrastructure and core proxy functionality for intercepting, authenticating, and forwarding LLM API requests.

## Features

- **API Key Authentication**: Secure access to the proxy via `Authorization: Bearer <token>` headers.
- **LLM API Proxying**: Routes requests to OpenAI, Anthropic Claude, and Azure OpenAI.
- **Health Checks**: `/health` and `/version` endpoints for monitoring.
- **Configuration**: Environment variable-based configuration for API keys, endpoints, and other settings.
- **Docker Support**: Containerized deployment using Docker.

## Running the Project

The recommended way to run PromptTrap for development is with Docker Compose. This handles all dependencies and provides a consistent environment.

### Prerequisites

- Docker and Docker Compose

### 1. Configure Environment Variables

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

### 2. Build and Run with Docker Compose

```bash
docker-compose up --build
```

The application will be running in a Docker container, accessible at `http://localhost:8000`. The server supports hot-reloading, so any changes you make to the code will be applied automatically.

### 3. Running Tests

To run the unit and integration tests, execute the following command while the container is running:

```bash
docker-compose exec prompttrap-gateway poetry run pytest
```

## API Endpoints

- `/health`: Health check endpoint.
- `/version`: Returns service version information.
- `/api/openai/{path:path}`: Proxies requests to the OpenAI API.
- `/api/claude/{path:path}`: Proxies requests to the Anthropic Claude API.
- `/api/azureopenai/{path:path}`: Proxies requests to the Azure OpenAI API.

For detailed API documentation, refer to `docs/api.md`.
For development documentation, refer to `docs/development.md`.

## Contributing

Contributions are welcome! Please refer to `CONTRIBUTING.md` for guidelines on setting up your development environment and contributing to the project.

## Licensing

- Core: [Apache 2.0 License](./LICENSE)
- Enterprise Features (e.g., policy engine, SSO, dashboard): [Enterprise License](./LICENSE-ENTERPRISE.txt)
