from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load .env based on ENV
env_name = os.getenv("ENV", "development")  # fallback to dev
load_dotenv(f".env.{env_name}")

class Settings(BaseSettings):
    ENV: str
    DATABASE_URL: str
    LOG_LEVEL: str
    API_KEY: str

    class Config:
        env_file = f".env.{env_name}"

settings = Settings()