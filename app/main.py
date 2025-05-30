# app/main.py
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import sample, gen_text
from app.core.logging_config import setup_logging
from app.core.config import settings
import logging


setup_logging()
logger = logging.getLogger(__name__)

# logger.setLevel(settings.LOG_LEVEL)
# print(f"🛠 Running in {settings.ENV} environment")


app = FastAPI(title="FastAPI Template")


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")



# Add CORS config(example)
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://example.com",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.info("🚀 FastAPI app is starting...")

app.include_router(sample.router, prefix="/api/v1")
app.include_router(gen_text.router, prefix="/api/v1")
