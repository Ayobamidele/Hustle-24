# from typing import Generic
from django.db import models
from shop.models import Product
import accounts.models

# Create your models here.

class WatchList(models.Model):
	group = models.ForeignKey("accounts.WatchGroup", on_delete=models.CASCADE, null=True, related_name="WatchGroup")
	customer = models.ForeignKey("accounts.Customer", on_delete=models.CASCADE, null=True, related_name="Customer")
	product =  models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	initial_Price = models.DecimalField(decimal_places=2,max_digits=100)
	initial_quantity = models.IntegerField(default=0)
	date_added = models.DateTimeField(auto_now_add=True)
	# owner = GenericForeignKey(customer,group)

	def __str__(self):
		return f"{self.date_added}|{self.id}"

class WatchedProduct(models.Model):
	watch_list = models.ForeignKey(WatchList, on_delete=models.CASCADE, null=False, related_name="WatchList")
	product =  models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	initial_Price = models.DecimalField(decimal_places=2,max_digits=100)
	initial_quantity = models.IntegerField(default=0)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.shopname