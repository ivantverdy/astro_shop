from django.db import models
import datetime

#categories
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
#customers
class Customer(models.Model):

#products
class Product(models.Model):

#orders
class Order(models.Model):