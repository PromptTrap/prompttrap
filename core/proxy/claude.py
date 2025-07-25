from fastapi import Request, Response
import httpx
from .. import config

async def proxy(request: Request, path: str):
    """Proxies requests to the Claude API."""
    async with httpx.AsyncClient() as client:
        url = f"{config.CLAUDE_BASE_URL}/{path}"
        headers = dict(request.headers)
        headers["x-api-key"] = config.CLAUDE_API_KEY
        rp = await client.post(url, json=await request.json(), headers=headers, timeout=config.REQUEST_TIMEOUT)
        return Response(content=rp.content, status_code=rp.status_code, headers=dict(rp.headers))
