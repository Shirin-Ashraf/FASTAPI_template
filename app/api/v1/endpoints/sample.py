# app/api/v1/endpoints/sample.py
from fastapi import APIRouter, Depends
from app.core.auth import verify_api_key
from app.core.logger import logger
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

# @router.get("/hello", dependencies=[Depends(verify_api_key)])
# def say_hello():
#     logger.info("Hello endpoint was called")
#     return {"message": "Hello! You are authenticated."}

@router.get("/hello")
def hello(name: str = "Developer", api_key: str = Depends(verify_api_key)):
    logger.info(f"✅ Accessed /hello endpoint with name={name}")
    return {"message": f"Hello, {name}! Your API is working."}