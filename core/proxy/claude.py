from fastapi import APIRouter, Request, Response, HTTPException
from fastapi.responses import JSONResponse
import httpx
from .. import config
import logging
import json

router = APIRouter()
logger = logging.getLogger(__name__)

EXCLUDED_RESPONSE_HEADERS = [
    "connection",
    "keep-alive",
    "proxy-authenticate",
    "proxy-authorization",
    "te",
    "trailers",
    "transfer-encoding",
    "upgrade",
    "content-encoding",
    "content-length",
]


@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def claude_proxy(request: Request, path: str):
    """Proxies requests to the Claude API."""
    if not config.CLAUDE_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="The server is not configured with a CLAUDE_API_KEY.",
        )

    base_url = config.CLAUDE_BASE_URL.rstrip("/")
    # The Claude API is versioned, e.g., /v1/messages
    url = f"{base_url}/v1/{path.lstrip('/')}"

    # Create a clean set of headers for the downstream request
    body = await request.json()
    req_headers = {
        "x-api-key": config.CLAUDE_API_KEY,
        "anthropic-version": request.headers.get("anthropic-version", "2023-06-01"),
        "content-type": "application/json",
    }

    async with httpx.AsyncClient() as client:
        try:
            req = client.build_request(
                method=request.method,
                url=url,
                headers=req_headers,
                json=body,
                timeout=config.REQUEST_TIMEOUT,
            )
            r = await client.send(req, stream=True)
            response_content = await r.aread()

        except httpx.RequestError as e:
            logger.error(f"Error proxying to {url}: {e}")
            raise HTTPException(
                status_code=502, detail=f"Error connecting to downstream service: {e}"
            )

    if r.status_code >= 400:
        logger.error(
            f"Error from downstream service at {url}: status={r.status_code} "
            f"response={response_content.decode(errors='ignore')}"
        )
        try:
            error_payload = json.loads(response_content)
            return JSONResponse(content=error_payload, status_code=r.status_code)
        except json.JSONDecodeError:
            raise HTTPException(
                status_code=502,
                detail="Proxy received an invalid (non-JSON) error response from downstream service.",
            )

    res_headers = {
        k: v
        for k, v in r.headers.items()
        if k.lower() not in EXCLUDED_RESPONSE_HEADERS
    }

    return Response(
        content=response_content,
        status_code=r.status_code,
        headers=res_headers,
    )