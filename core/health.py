from fastapi import APIRouter
import time

router = APIRouter()

start_time = time.time()

@router.get("/health")
def health():
    """Returns the health of the service."""
    return {
        "status": "healthy",
        "timestamp": time.time(),
        "uptime": time.time() - start_time,
    }

@router.get("/version")
def version():
    """Returns the version of the service."""
    return {
        "version": "0.1.0",
        "build": "abc1234",
        "python_version": "3.11.5",
    }
