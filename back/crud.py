# crud.py
from sqlalchemy.orm import Session
from models import Recipe

def create_recipe(db: Session, recipe_data: dict):
    db_recipe = Recipe(**recipe_data)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

def get_recipes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Recipe).offset(skip).limit(limit).all()
