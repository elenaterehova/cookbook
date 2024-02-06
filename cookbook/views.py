from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeIngredients, Product


def add_product_to_recipe(request: HttpRequest, recipe_id, product_id, weight):
    recipe = Recipe.objects.get(id=recipe_id)
    product = Product.objects.get(id=product_id)
    recipe_ingredient, created = RecipeIngredients.objects.update_or_create(
        recipe=recipe,
        ingredient=product,
        defaults={'weight': weight}
    )
    recipe_ingredient.save()
    return HttpResponse('Success')


def cook_recipe(request: HttpRequest, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if recipe is not None:
        for ingredient in recipe.ingredients.all():
            ingredient.recipes_count += 1
            ingredient.save()
        return HttpResponse('Success')
    return HttpResponse('Not found')


def show_recipes_without_product(request: HttpRequest, product_id):
    product = Product.objects.get(id=product_id)
    recipes = Recipe.objects.exclude(ingredients=product_id, recipeingredients__weight__lte=10)
    return render(request, 'recipes_without_product.html', {
        'recipes': recipes,
        'product_name': product.name,
    })
