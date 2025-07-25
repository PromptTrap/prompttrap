import pytest
from fastapi.testclient import TestClient
from core.main import app
from core import config
import os

@pytest.fixture(scope="module")
def client():
    # Set environment variables for testing
    os.environ["PROMPTTRAP_API_KEYS"] = "key1"
    os.environ["OPENAI_API_KEY"] = "test_openai_key"
    os.environ["CLAUDE_API_KEY"] = "test_claude_key"
    os.environ["AZURE_OPENAI_API_KEY"] = "test_azure_key"
    os.environ["AZURE_OPENAI_ENDPOINT"] = "https://your-resource.openai.azure.com"

    # Directly set config values for tests
    config.PROMPTTRAP_API_KEYS = ["key1"]
    config.OPENAI_API_KEY = "test_openai_key"
    config.CLAUDE_API_KEY = "test_claude_key"
    config.AZURE_OPENAI_API_KEY = "test_azure_key"
    config.AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com"

    with TestClient(app) as c:
        yield c

    # Clean up environment variables after tests
    del os.environ["PROMPTTRAP_API_KEYS"]
    del os.environ["OPENAI_API_KEY"]
    del os.environ["CLAUDE_API_KEY"]
    del os.environ["AZURE_OPENAI_API_KEY"]
    del os.environ["AZURE_OPENAI_ENDPOINT"]
