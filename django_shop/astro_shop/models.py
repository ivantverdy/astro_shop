from django.db import models
import datetime

#categories
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
#customers
class Customer(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=16)
    password = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

#products
class Product(models.Model):

#orders
class Order(models.Model):