# Generated by Django 5.0.1 on 2024-02-03 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cookbook', '0002_alter_product_recipes_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredients',
            old_name='product',
            new_name='recipe',
        ),
    ]