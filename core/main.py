from fastapi import FastAPI, Depends
from . import config
from . import health
from .proxy.openai_proxy import router as openai_router
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
app.include_router(openai_router, prefix="/api/openai", dependencies=[Depends(get_token)])