from django.db import models

class Wine(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    aged = models.IntegerField()
    cellar = models.CharField(max_length=50)

class Cellar(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)

class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()