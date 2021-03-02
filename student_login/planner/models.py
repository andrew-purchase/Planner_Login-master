from django.db import models


# Create your models here.
class Courses(models.Model):
    Courses = models.CharField(max_length=15)
    Fall2018 = models.CharField(max_length=15)
    Spring2019 = models.CharField(max_length=15)
    Fall2019 = models.CharField(max_length=15)
    Spring2020 = models.CharField(max_length=15)
    Fall2020 = models.CharField(max_length=15)
    Spring2021 = models.CharField(max_length=15)
    Fall2021 = models.CharField(max_length=15)
    Spring2022 = models.CharField(max_length=15)



