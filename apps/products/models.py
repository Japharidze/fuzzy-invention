from django.db import models

class Product(models.Model):
    name = models.CharField(200)
    price = models.FloatField
    description = models.TextField

