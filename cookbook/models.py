from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    recipes_count = models.IntegerField(verbose_name='Количество использования', default=0)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=150, default="", verbose_name='Название рецепта')
    ingredients = models.ManyToManyField(Product, through='RecipeIngredients')

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self):
        return self.title


class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Рецепт")
    ingredient = models.ForeignKey(Product, on_delete=models.CASCADE, default="", verbose_name='Ингредиент')
    weight = models.PositiveIntegerField(default=0, verbose_name='Количество (в граммах)')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        unique_together = ('recipe', 'ingredient')

    def __str__(self):
        return self.ingredient.name
