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


if __name__ == "__main__":
    import uvicorn
