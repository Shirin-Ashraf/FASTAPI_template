from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from app.core.config import settings

# DATABASE_URL = "postgresql://tester:shirin@172.30.109.106:5432/sample_db"

# engine = create_engine(DATABASE_URL)  
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DATABASE_URL = settings.DATABASE_URL
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()