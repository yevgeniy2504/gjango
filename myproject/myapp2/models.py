from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    image = models.ImageField(upload_to="products/")


class Order2(models.Model):
    costumer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    datte_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)



