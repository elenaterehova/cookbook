from django.contrib import admin
from .models import Recipe, Product, RecipeIngredient

admin.site.register(Recipe)
admin.site.register(Product)
admin.site.register(RecipeIngredient)