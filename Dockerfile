FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install poetry
RUN pip install poetry

# Copy only dependency definition files
COPY pyproject.toml poetry.lock* ./

# Install dependencies
# Using --no-root because the project code will be mounted as a volume
RUN poetry config virtualenvs.create false && \
    poetry install --no-root --only main

# The application code will be mounted via a volume in docker-compose.
# This avoids copying it into the image, ensuring that live-reloading
# always uses the host's files.

EXPOSE 8000

# The command is specified in docker-compose.yml to enable reloading.