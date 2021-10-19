from django.db import models
from shop.models import Product
from accounts.models import Customer
# Create your models here.

class Cart(models.Model):
	customer = models.OneToOneField(Customer ,on_delete=models.CASCADE, null=True)
	products = models.ManyToManyField(Product)
	totalprice = models.DecimalField(max_digits=1000000000000,decimal_places=2, default=0.00)
	quantity = models.IntegerField(default=1)
	ordered = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.id)

class OrderItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, null=True)
    is_ordered = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    date_ordered = models.DateTimeField(null=True)

    def __str__(self):
        return self.product.name

class Order(models.Model):
	ref_code = models.CharField(max_length=15)
	owner = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	is_ordered = models.BooleanField(default=False)
	items = models.ManyToManyField(OrderItem)
	quantity = models.IntegerField(default=1)
	price = models.DecimalField(max_digits=1000000000000000000,decimal_places=2, default=0.00)
	date_ordered = models.DateTimeField(auto_now=True)

	def get_cart_items(self):
		return self.items.all()

	def get_cart_total(self):
		return sum([item.product.price for item in self.items.all()])

	def __str__(self):
		return '{0} - {1}'.format(self.owner, self.ref_code)