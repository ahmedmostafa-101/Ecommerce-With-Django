
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)
    desc = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    name = models.CharField(max_length=200,unique=True)
    desc = models.TextField(max_length=5000)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    cat_id = models.ForeignKey(Category,related_name='product',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='product',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# class OrderItem(models.Model):
#     user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
#     ordered = models.BooleanField(default=False)
#     item = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField(default=1)


# class Cart(models.Model):
#     user = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
#     products = models.ManyToManyField(OrderItem, blank=True)
#     subtotal = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
#     total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
#     updated = models.DateTimeField(auto_now=True)
#     ordered = models.BooleanField(default=False)
#     session_key = models.CharField(max_length=40, null=True)
    