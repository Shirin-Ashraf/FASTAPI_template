📘 Demo: Integrating a Sample Script & Exposing It as an API

This guide demonstrates how to integrate a simple script into the FastAPI Template and expose it as an API endpoint.

🧠 Step 1: Create Your Script

Example script: sentiment_analyzer.py

# app/sentiment_analyzer.py
def analyze_sentiment(text: str) -> str:
    """A mock sentiment analysis function"""
    text = text.lower()
    if "good" in text:
        return "Positive"
    elif "bad" in text:
        return "Negative"
    return "Neutral"

🛤️ Step 2: Create an Endpoint File

Create sentiment.py under app/api/v1/endpoints/

# app/api/v1/endpoints/sentiment.py
from fastapi import APIRouter, Depends, Request
from app.core.auth import verify_api_key
from app.sentiment_analyzer import analyze_sentiment
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/sentiment")
async def detect_sentiment(request: Request, payload: dict, api_key: str = Depends(verify_api_key)):
    text = payload.get("text", "")
    sentiment = analyze_sentiment(text)
    logger.info(f"Sentiment detected: {sentiment}")
    return {"sentiment": sentiment}

🧩 Step 3: Register the Endpoint

Update main.py to include your new router:

from app.api.v1.endpoints import sentiment
...
app.include_router(sentiment.router, prefix="/api/v1")

📦 Step 4: Test the Endpoint

Run the app:

uvicorn app.main:app --reload

Test with curl:

curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/sentiment' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: your_api_key_here' \
  -d '{"text": "This is a good day"}'

Response:

{
  "sentiment": "Positive"
}

✅ Done!

You’ve now successfully integrated and exposed a custom script as an API.