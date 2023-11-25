# create_tables.py
from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
import os
from models import Base
# from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()

# Use a relative path to create the database file in the current working directory
DATABASE_URL = f"sqlite:///{os.path.join(os.getcwd(), 'recipes.db')}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)
