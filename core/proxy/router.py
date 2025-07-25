from fastapi import APIRouter, Request
from . import openai, claude, azure

router = APIRouter()

@router.post("/openai/{path:path}")
async def proxy_openai(request: Request, path: str):
    """Proxies requests to the OpenAI API."""
    return await openai.proxy(request, path)

@router.post("/claude/{path:path}")
async def proxy_claude(request: Request, path: str):
    """Proxies requests to the Claude API."""
    return await claude.proxy(request, path)

@router.post("/azure/{path:path}")
async def proxy_azure(request: Request, path: str):
    """Proxies requests to the Azure OpenAI API."""
    return await azure.proxy(request, path)
