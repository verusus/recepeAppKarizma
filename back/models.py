# models.py
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    ingredients = Column(Text)
    how_to_prepare = Column(Text)
    time_to_cook = Column(String)
    optional_image = Column(String, nullable=True)
    created_at = Column(String, server_default=func.now())
