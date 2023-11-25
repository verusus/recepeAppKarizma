// src/app/recipe-list/recipe-list.component.ts
import { Component, OnInit } from '@angular/core';
import { RecipeService } from '../recipe.service';

@Component({
  selector: 'app-recipe-list',
  templateUrl: './recipe-list.component.html',
  styleUrls: ['./recipe-list.component.css']
})
export class RecipeListComponent implements OnInit {
  recipes?: any[];

  constructor(private recipeService: RecipeService) { }

  ngOnInit(): void {
    this.loadRecipes();
  }

  loadRecipes(): void {
    this.recipeService.getRecipes().subscribe(
      (data) => {
        this.recipes = data;
      },
      (error) => {
        console.error('Error fetching recipes:', error);
      }
    );
  }
}
