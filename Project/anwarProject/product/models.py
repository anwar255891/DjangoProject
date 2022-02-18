from django.db import models


# Create your models here.

class Product(models.Model):
    '''name, weight, price, created_at, updated_at'''
    name=models.CharField(max_length=50)
    weight=models.DecimalField(max_digits=4,decimal_places=2)
    price=models.PositiveBigIntegerField()
    created_at=models.DateField(max_length=50)
    updates_at=models.DateField(max_length=50)
