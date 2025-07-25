from fastapi import APIRouter, Request, Response, HTTPException
from fastapi.responses import JSONResponse
import httpx
from .. import config
import logging
import json

router = APIRouter()

logger = logging.getLogger(__name__)

# Headers that should not be forwarded from the client request.
# Based on https://www.rfc-editor.org/rfc/rfc2616#section-13.5.1
EXCLUDED_REQUEST_HEADERS = [
    "connection",
    "keep-alive",
    "proxy-authenticate",
    "proxy-authorization",
    "te",
    "trailers",
    "transfer-encoding",
    "upgrade",
    "host",  # Will be set by the proxy
]

# Headers that should not be forwarded from the downstream response.
EXCLUDED_RESPONSE_HEADERS = [
    "connection",
    "keep-alive",
    "proxy-authenticate",
    "proxy-authorization",
    "te",
    "trailers",
    "transfer-encoding",
    "upgrade",
    "content-encoding",  # Let Starlette handle it
    "content-length",  # Let Starlette handle it
]


@router.api_route("/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(request: Request, path: str):
    """Proxies requests to the OpenAI API."""
    if not config.OPENAI_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="The server is not configured with an OPENAI_API_KEY.",
        )

    base_url = config.OPENAI_BASE_URL.rstrip("/")
    request_path = path.lstrip("/")

    # Prevent duplicating the API version (e.g., 'v1') in the path
    base_path_last_part = base_url.split("/")[-1]
    if request_path.startswith(base_path_last_part):
        request_path = request_path[len(base_path_last_part) :].lstrip("/")

    url = f"{base_url}/{request_path}"

    # Create a clean set of headers, only forwarding what's necessary.
    req_headers = {
        "Authorization": f"Bearer {config.OPENAI_API_KEY}",
    }
    body = await request.body()
    if body:
        req_headers["Content-Type"] = "application/json"

    async with httpx.AsyncClient() as client:
        try:
            req = client.build_request(
                method=request.method,
                url=url,
                headers=req_headers,
                content=body,
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
