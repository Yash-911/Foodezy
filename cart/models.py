from urllib import request

from django.db import models
from django.contrib.auth.models import User

class Cart(models.Model):
    cust_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    recipe_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="foodimages/")
    price = models.IntegerField()
    final_price = models.IntegerField()
    ticked = models.BooleanField(default=False)
    def __str__(self):
        return self.recipe_name


class Checkout(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    address=models.CharField(max_length=50)
    address2=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    zip=models.IntegerField()
    userid=models.IntegerField(null=True)
    Amount=models.IntegerField(null=True)


    def __str__(self):
        return self.name




