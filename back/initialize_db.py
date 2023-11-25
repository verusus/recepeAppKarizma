# initialize_db.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "sqlite:///./recipes.db"  # Use your preferred database URL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def initialize_db():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    initialize_db()
