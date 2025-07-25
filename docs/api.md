# PromptTrap API Documentation

This document provides a detailed overview of the API endpoints exposed by the PromptTrap gateway.

## Base URL

The base URL for all API endpoints is `http://localhost:8000` when running locally.

## Authentication

All proxy endpoints (`/api/openai`, `/api/claude`, `/api/azureopenai`) require API key-based authentication via the `Authorization` header.

**Header:** `Authorization: Bearer <YOUR_PROMPTTRAP_API_KEY>`

Replace `<YOUR_PROMPTTRAP_API_KEY>` with a key configured in your PromptTrap instance (e.g., in the `.env` file via `PROMPTTRAP_API_KEYS`).

## Endpoints

### 1. Health Check

Checks the operational status of the PromptTrap service.

- **GET `/health`**

  **Description:** Returns the current health status, timestamp, and uptime of the service.

  **Response (200 OK):**
  ```json
  {
    "status": "healthy",
    "timestamp": "2025-01-15T10:30:00Z",
    "uptime": 3600
  }
  ```

### 2. Version Information

Retrieves version and build information about the PromptTrap service.

- **GET `/version`**

  **Description:** Returns the version, build identifier, and Python version used by the service.

  **Response (200 OK):**
  ```json
  {
    "version": "0.1.0",
    "build": "abc1234",
    "python_version": "3.11.5"
  }
  ```

### 3. OpenAI Proxy

Proxies requests to the OpenAI API. All paths following `/api/openai/` will be forwarded to the configured OpenAI base URL.

- **POST `/api/openai/{path:path}`**

  **Description:** Forwards the request body and headers (injecting the OpenAI API key) to the corresponding OpenAI endpoint.

  **Path Parameters:**
  - `path` (string, required): The specific OpenAI API endpoint path (e.g., `v1/chat/completions`, `v1/embeddings`).

  **Request Body:** The request body should match the expected payload for the target OpenAI API endpoint.

  **Headers:**
  - `Authorization: Bearer <YOUR_PROMPTTRAP_API_KEY>` (for PromptTrap authentication)
  - Other headers will be forwarded to OpenAI.

  **Example (cURL):**
  ```bash
  curl -X POST \
    http://localhost:8000/api/openai/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer your_secret_prompttrap_key" \
    -d '{ "model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "Hello!"}] }'
  ```

### 4. Anthropic Claude Proxy

Proxies requests to the Anthropic Claude API. All paths following `/api/claude/` will be forwarded to the configured Claude base URL.

- **POST `/api/claude/{path:path}`**

  **Description:** Forwards the request body and headers (injecting the Claude API key) to the corresponding Claude endpoint.

  **Path Parameters:**
  - `path` (string, required): The specific Claude API endpoint path (e.g., `v1/messages`).

  **Request Body:** The request body should match the expected payload for the target Claude API endpoint.

  **Headers:**
  - `Authorization: Bearer <YOUR_PROMPTTRAP_API_KEY>` (for PromptTrap authentication)
  - Other headers will be forwarded to Claude.

  **Example (cURL):**
  ```bash
  curl -X POST \
    http://localhost:8000/api/claude/v1/messages \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer your_secret_prompttrap_key" \
    -d '{ "model": "claude-3-opus-20240229", "messages": [{"role": "user", "content": "Hello!"}] }'
  ```

### 5. Azure OpenAI Proxy

Proxies requests to the Azure OpenAI API. All paths following `/api/azureopenai/` will be forwarded to the configured Azure OpenAI endpoint.

- **POST `/api/azureopenai/{path:path}`**

  **Description:** Forwards the request body and headers (injecting the Azure OpenAI API key) to the corresponding Azure OpenAI endpoint.

  **Path Parameters:**
  - `path` (string, required): The specific Azure OpenAI API endpoint path (e.g., `openai/deployments/your-deployment-name/chat/completions?api-version=2024-02-15-preview`).

  **Request Body:** The request body should match the expected payload for the target Azure OpenAI API endpoint.

  **Headers:**
  - `Authorization: Bearer <YOUR_PROMPTTRAP_API_KEY>` (for PromptTrap authentication)
  - Other headers will be forwarded to Azure OpenAI.

  **Example (cURL):**
  ```bash
  curl -X POST \
    http://localhost:8000/api/azureopenai/openai/deployments/your-deployment-name/chat/completions?api-version=2024-02-15-preview \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer your_secret_prompttrap_key" \
    -d '{ "messages": [{"role": "user", "content": "Hello!"}] }'
  ```
