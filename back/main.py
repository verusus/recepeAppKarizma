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

# Endpoint to update a recipe by ID
@app.put("/recipes/{recipe_id}")
def update_recipe(recipe_id: int, recipe_data: dict, db: Session = Depends(get_db)):
    existing_recipe = crud.get_recipe_by_id(db, recipe_id)
    if existing_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    updated_recipe = crud.update_recipe(db, existing_recipe, recipe_data)
    return updated_recipe

# Endpoint to delete a recipe by ID
@app.delete("/recipes/{recipe_id}")
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    existing_recipe = crud.get_recipe_by_id(db, recipe_id)
    if existing_recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")

    crud.delete_recipe(db, existing_recipe)
    return {"message": "Recipe deleted successfully"}
