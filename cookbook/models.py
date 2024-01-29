from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True)
    recipes_count = models.IntegerField()

    def __str__(self):
        return self.name


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Product, models.CASCADE)
    recipe = models.ForeignKey("Recipe", models.CASCADE)
    amount = models.IntegerField()
    unit_of_measure = models.CharField(blank=True, max_length=20)

    def __str__(self):
        return str(self.ingredient) + " " + str(self.amount)


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField(Product, through=RecipeIngredient)

    def __str__(self):
        return self.name

