from django.db import models


# Create your models here.
class Users(models.Model):
    ID = models.CharField(max_length=9)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)



