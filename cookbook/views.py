from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeIngredients, Product


def post_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def cook_recipe(request: HttpRequest, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe is not None:
        for ingredient in recipe.ingredients.all():
            ingredient.recipes_count += 1
            ingredient.save()
        return HttpResponse('Success')
    return HttpResponse('Not found')
