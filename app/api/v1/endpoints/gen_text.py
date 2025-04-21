# app/api/v1/endpoints/gen_text.py

from fastapi import APIRouter, Depends, Request
from app.core.auth import verify_api_key
from app.gen_text_generator import generate_text
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/generate")
async def generate(request: Request, payload: dict, api_key: str = Depends(verify_api_key)):
    # verify_api_key(request)
    prompt = payload.get("prompt", "")
    response = generate_text(prompt)
    return {"generated_text": response}
