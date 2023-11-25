# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import database

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
# Endpoint to create a recipe
@app.post("/recipes/")
def create_recipe(recipe_data: dict, db: Session = Depends(get_db)):
    return crud.create_recipe(db, recipe_data)

# Endpoint to get a list of recipes
@app.get("/recipes/")
def read_recipes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    recipes = crud.get_recipes(db, skip=skip, limit=limit)
    return recipes
