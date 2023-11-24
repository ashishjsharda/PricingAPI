from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    discount = models.FloatField()

from rest_framework import serializers
from .models import Product, Offer

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'stock', 'image_url']


