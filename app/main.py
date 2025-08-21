"""
TrackMind - Main Application Entry Point
Платформа аналитики пользовательского поведения
"""

import logging

from fastapi import FastAPI, Request, HTTPException

from app.core.config import settings
from app.core.logging import setup_logging


setup_logging()
logger = logging.getLogger(__name__)


app = FastAPI(
    title="TrackMind",
    description="Платформа аналитики пользовательского поведения",
    version="0.1.0",
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None,
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )
