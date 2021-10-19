from django.db import models
from shop.models import Product
from accounts.models import Customer
# Create your models here.

class Cart(models.Model):
	customer = models.OneToOneField(Customer ,on_delete=models.SET_NULL, null=False)
	products = models.ManyToManyField(Product ,on_delete=models.CASCADE)
	totalprice = models.DecimalField(max_digits=1000000000000,decimal_places=2, default=0.00)
	quantity = models.IntegerField(default=1)
	ordered = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name