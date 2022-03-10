from django.db import models
from shop.models import Product
from accounts.models import Customer

# Create your models here.
class WishList(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, related_name="Customer")
	product =  models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	initial_Price = models.DecimalField(decimal_places=2,max_digits=100)
	initial_quantity = models.IntegerField(default=0)
	date_added = models.DateTimeField(auto_now_add=True)
