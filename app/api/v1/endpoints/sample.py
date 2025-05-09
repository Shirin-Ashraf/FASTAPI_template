from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.auth import verify_api_key
from app.core.logger import logger
from app.db import crud, database, models
from pydantic import BaseModel, EmailStr

router = APIRouter()


# Dependency injection to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for input validation
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
    
    # Save to DB
    try:
        user = crud.create_user(db=db, name=payload.name, email=payload.email, age=payload.age)
    except Exception as e:
        logger.error(f"❌ Error saving to DB: {e}")
        raise HTTPException(status_code=400, detail="Could not save user. Email might already exist.")

    return {"message": f"Hello, {payload.name}! Your email {payload.email} has been saved."}

