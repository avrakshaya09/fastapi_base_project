from fastapi import FastAPI
from src.routers import health


def create_app() -> FastAPI:
    app = FastAPI(title="Base FastAPI App")
    app.include_router(health.router)
    return app
