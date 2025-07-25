# PromptTrap Deployment Guide

This guide provides instructions for deploying the PromptTrap gateway using Docker.

## 1. Docker Deployment

PromptTrap is designed to be deployed as a Docker container, providing a consistent and isolated environment.

### Prerequisites

- **Docker**: Ensure Docker is installed and running on your deployment environment.

### Steps

1.  **Clone the Repository:**
    If you haven't already, clone the PromptTrap repository to your deployment server:
    ```bash
    git clone https://github.com/your-org/prompttrap.git
    cd prompttrap
    ```

2.  **Configure Environment Variables:**
    Create a `.env` file in the project root directory. This file will contain sensitive information like API keys and other configuration settings that should not be committed to version control.

    Copy the example environment file:
    ```bash
    cp .env.example .env
    ```

    Edit the `.env` file and replace the placeholder values with your actual API keys and desired configurations. For production deployments, ensure these keys are secure and managed appropriately.

    ```ini
    # Example .env content for deployment
    PROMPTTRAP_HOST=0.0.0.0
    PROMPTTRAP_PORT=8000
    PROMPTTRAP_LOG_LEVEL=INFO
    PROMPTTRAP_CORS_ORIGINS=*

    PROMPTTRAP_API_KEYS=your_secret_prompttrap_key

    OPENAI_API_KEY=sk-your-openai-key
    OPENAI_BASE_URL=https://api.openai.com/v1
    CLAUDE_API_KEY=sk-ant-your-claude-key
    CLAUDE_BASE_URL=https://api.anthropic.com
    AZURE_OPENAI_API_KEY=your-azure-openai-key
    AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com

    REQUEST_TIMEOUT=30
    MAX_REQUEST_SIZE=10485760
    ```

3.  **Build the Docker Image:**
    From the project root directory, build the Docker image using `docker-compose`. This will build the `prompttrap-gateway` service as defined in `docker-compose.yml`.
    ```bash
    docker-compose build
    ```
    This command will execute the multi-stage build defined in the `Dockerfile`, first installing dependencies and then creating a lean production image.

4.  **Run the Docker Container:**
    Once the image is built, you can run the container using `docker-compose`:
    ```bash
    docker-compose up -d
    ```
    The `-d` flag runs the containers in detached mode (in the background).

    The PromptTrap API will be accessible on port `8000` of your host machine (or the port you configured in `docker-compose.yml`).

    To verify that the container is running:
    ```bash
    docker-compose ps
    ```

5.  **Stopping the Container:**
    To stop the running PromptTrap container:
    ```bash
    docker-compose down
    ```

## 2. Production Considerations

### Security

- **API Key Management**: Do not hardcode API keys in your `.env` file in production. Use a secure secrets management solution (e.g., Kubernetes Secrets, AWS Secrets Manager, Azure Key Vault) to inject environment variables into your containers.
- **Network Security**: Configure firewalls and network security groups to restrict access to the PromptTrap API only from trusted sources.
- **HTTPS**: Always deploy PromptTrap behind a reverse proxy (e.g., Nginx, Caddy, Traefik) that handles SSL/TLS termination to ensure all traffic is encrypted.

### Scalability and High Availability

- **Load Balancing**: For high traffic, deploy multiple instances of the PromptTrap container behind a load balancer.
- **Container Orchestration**: Use container orchestration platforms like Kubernetes, Docker Swarm, or AWS ECS to manage, scale, and monitor your PromptTrap deployments.

### Logging and Monitoring

- **Centralized Logging**: Configure your Docker environment to send container logs to a centralized logging system (e.g., ELK stack, Splunk, Datadog).
- **Monitoring**: Set up monitoring for container health, resource utilization (CPU, memory), and API request metrics (latency, error rates).

### Updates and Rollbacks

- Implement a robust deployment strategy that allows for zero-downtime updates and easy rollbacks in case of issues.
