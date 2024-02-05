from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404
from .models import Recipe, RecipeIngredients, Product


def post_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


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
