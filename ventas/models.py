from django.db import models
from inventario.models import Product

class Invoice(models.Model):
    detail = models.CharField(max_length=255)
    products = models.ManyToManyField(Product) 
    
