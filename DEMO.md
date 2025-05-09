# 📘 Demo: Creating a Sample User API with DB Integration

This guide demonstrates how to expose a custom Python function with database interaction using the FastAPI Template.


## Step 1: Define Your Input & Logic

We are collecting user data (name, email, age) and saving it to a database using SQLAlchemy.

Create a `crud.py` function to handle database interaction:

### app/db/crud.py

from sqlalchemy.orm import Session
from app.db import models

def create_user(db: Session, name: str, email: str, age: int):
    user = models.User(name=name, email=email, age=age)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


Make sure you have a corresponding SQLAlchemy model (`User`) defined in `models.py`.

## Step 2: Setup Your Database Connection

You also need a database.py file where your SQLAlchemy session is initialized:

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # Replace with your DB URL

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

## Step 3: Create an Endpoint File

Create `sample.py` under `app/api/`:


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.auth import verify_api_key
from app.core.logger import logger
from app.db import crud, database, models
from pydantic import BaseModel, EmailStr

router = APIRouter()

## Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

## Input schema
class UserInput(BaseModel):
    name: str
    email: EmailStr
    age: int

@router.post("/hello")
def hello(
    payload: UserInput,
    api_key: str = Depends(verify_api_key),
    db: Session = Depends(get_db)
):
    logger.info(f"✅ Accessed /hello with name={payload.name} and email={payload.email}")
    
    try:
        user = crud.create_user(db=db, name=payload.name, email=payload.email, age=payload.age)
    except Exception as e:
        logger.error(f"❌ Error saving to DB: {e}")
        raise HTTPException(status_code=400, detail="Could not save user. Email might already exist.")

    return {"message": f"Hello, {payload.name}! Your email {payload.email} has been saved."}


## Step 4: Register the Endpoint

Update `main.py` to include the router:

from fastapi import FastAPI
from app.api import sample

app = FastAPI()

app.include_router(sample.router, prefix="/api")


## Step 5: Test the Endpoint

Start your server:


uvicorn app.main:app --reload


Send a test request using `curl`:


curl -X POST http://127.0.0.1:8000/api/hello \
  -H "Content-Type: application/json" \
  -H "X-API-Key: your_api_key_here" \
  -d '{"name": "Alice", "email": "alice@example.com", "age": 25}'


✅ Expected Response:


{
  "message": "Hello, Alice! Your email alice@example.com has been saved."
}
 


To run your FastAPI app in dev or prod mode, you can use environment variables to control the environment, e.g. ENV=dev or ENV=prod, and then conditionally load settings (like DB URL, logging level, etc.) accordingly.

## 1. Add an ENV variable in your .env file

## .env.dev

ENV=dev
DATABASE_URL=sqlite:///./dev.db

## .env.prod

ENV=prod
DATABASE_URL=postgresql://user:pass@host/db

## 2. Update your config.py to use this

### app/core/config.py
from pydantic import BaseSettings
import os
from dotenv import load_dotenv

## Load correct .env file based on ENV
env_type = os.getenv("ENV", "dev")
dotenv_file = f".env.{env_type}" if env_type != "dev" else ".env"
load_dotenv(dotenv_file)

class Settings(BaseSettings):
    ENV: str = os.getenv("ENV", "dev")
    DATABASE_URL: str = os.getenv("DATABASE_URL")

settings = Settings()

## 3. Use it throughout your app

### app/db/database.py
from app.core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

## 4. Run the app with a specific environment
For dev:

ENV=dev uvicorn app.main:app --reload


### ✅ Done!

You've now exposed a full FastAPI endpoint that:

* Accepts structured input using Pydantic
* Verifies an API key for security
* Persists data to a database
* Returns a clean JSON response

You can use this as a template to create more endpoints in your project!
