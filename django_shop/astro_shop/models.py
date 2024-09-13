from django.db import models


# categories
class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


# products
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=256, default='', blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


# orders
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=16)
    address = models.CharField(max_length=256)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} ordered {self.product.name}'
