import os
from dotenv import load_dotenv

load_dotenv()

PROMPTTRAP_HOST = os.getenv("PROMPTTRAP_HOST", "0.0.0.0")
PROMPTTRAP_PORT = int(os.getenv("PROMPTTRAP_PORT", 8000))
PROMPTTRAP_LOG_LEVEL = os.getenv("PROMPTTRAP_LOG_LEVEL", "INFO")
PROMPTTRAP_CORS_ORIGINS = os.getenv("PROMPTTRAP_CORS_ORIGINS", "*").split(",")
PROMPTTRAP_API_KEYS = os.getenv("PROMPTTRAP_API_KEYS", "").split(",")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
CLAUDE_BASE_URL = os.getenv("CLAUDE_BASE_URL", "https://api.anthropic.com")

AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")

REQUEST_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", 30))
MAX_REQUEST_SIZE = int(os.getenv("MAX_REQUEST_SIZE", 10485760))
