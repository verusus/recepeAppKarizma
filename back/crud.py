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

def get_recipe_by_id(db: Session, recipe_id: int):
    return db.query(Recipe).filter(Recipe.id == recipe_id).first()

def update_recipe(db: Session, existing_recipe: Recipe, recipe_data: dict):
    for key, value in recipe_data.items():
        setattr(existing_recipe, key, value)
    db.commit()
    db.refresh(existing_recipe)
    return existing_recipe

def delete_recipe(db: Session, recipe: Recipe):
    db.delete(recipe)
    db.commit()