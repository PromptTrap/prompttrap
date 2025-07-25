from fastapi import Request, Response
import httpx
from .. import config

async def proxy(request: Request, path: str):
    """Proxies requests to the Azure OpenAI API."""
    async with httpx.AsyncClient() as client:
        url = f"{config.AZURE_OPENAI_ENDPOINT}/{path}"
        headers = dict(request.headers)
        headers["api-key"] = config.AZURE_OPENAI_API_KEY
        rp = await client.post(url, json=await request.json(), headers=headers, timeout=config.REQUEST_TIMEOUT)
        return Response(content=rp.content, status_code=rp.status_code, headers=dict(rp.headers))
