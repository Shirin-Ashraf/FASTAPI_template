# app/main.py
from fastapi import FastAPI
from app.api.v1.endpoints import sample, gen_text
from app.core.logging_config import setup_logging
import logging

setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title="FastAPI Template")

logger.info("🚀 FastAPI app is starting...")

app.include_router(sample.router, prefix="/api/v1")
app.include_router(gen_text.router, prefix="/api/v1")
