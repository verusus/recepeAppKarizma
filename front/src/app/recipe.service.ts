// src/app/recipe.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class RecipeService {
  private apiUrl = 'http://127.0.0.1:8000';  

  constructor(private http: HttpClient) { }

  getRecipes(): Observable<any> {
    return this.http.get(`${this.apiUrl}/recipes/`);
  }

  createRecipe(recipeData: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/recipes/`, recipeData);
  }

  updateRecipe(recipeId: number, recipeData: any): Observable<any> {
    return this.http.put(`${this.apiUrl}/recipes/${recipeId}`, recipeData);
  }

  deleteRecipe(recipeId: number): Observable<any> {
    return this.http.delete(`${this.apiUrl}/recipes/${recipeId}`);
  }
}
