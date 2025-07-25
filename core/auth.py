from fastapi import Request, HTTPException
from . import config

async def get_token(request: Request):
    """Validates the token from the Authorization header."""
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Missing authorization header")

    if not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token type")

    token = token.split(" ")[1]
    if token not in config.PROMPTTRAP_API_KEYS:
        raise HTTPException(status_code=401, detail="Invalid token")

    return token
