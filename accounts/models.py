from django.db import models

class user(models.Model):
    id=models.AutoField(primary_key=True)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password1 = models.CharField(max_length=25)
    password2 = models.CharField(max_length=25)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


