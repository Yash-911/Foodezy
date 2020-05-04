from django.db import models


class Recipes(models.Model):
    recipe_name=models.CharField(max_length=50)
    image = models.ImageField(upload_to="foodimages/")
    cuisine = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    range1 = models.CharField(max_length=20)
    range2 = models.CharField(max_length=20)
    ingredients = models.CharField(max_length=20000)
    recipe = models.CharField(max_length=20000)
    note = models.CharField(max_length=5000)

    def __str__(self):
        return self.recipe_name

