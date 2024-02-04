from django.contrib import admin
from .models import (Recipe, RecipeIngredients, Product)

admin.site.register(RecipeIngredients)


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredients
    readonly_fields = ('id',)
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'recipes_count')
    readonly_fields = ('recipes_count',)
