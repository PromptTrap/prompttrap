from fastapi import FastAPI, Depends
from . import config
from . import health
from .proxy.router import router as proxy_router
from .auth import get_token
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=config.PROMPTTRAP_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(proxy_router, prefix="/api", dependencies=[Depends(get_token)])