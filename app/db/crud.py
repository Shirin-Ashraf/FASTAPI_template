from sqlalchemy.orm import Session
from app.db import models


def create_user(db: Session, name: str, email: str, age: int):
    user = models.User(name=name, email=email, age=age)
    db.add(user)
    db.commit()
    db.refresh(user)

    return user