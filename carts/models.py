from django.db import models
from shop.models import Product
from accounts.models import Customer
# Create your models here.

class Cart(models.Model):
	customer = models.OneToOneField(Customer ,on_delete=models.CASCADE, null=True)
	products = models.ManyToManyField(Product)
	totalprice = models.DecimalField(max_digits=1000000000000,decimal_places=2, default=0.00)
	quantity = models.IntegerField(default=0)
	ordered = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	active = models.BooleanField(default=True)

	def __str__(self):
		return str(self.id)


class Order(models.Model):
	ref_code = models.CharField(max_length=200, null=True)
	Cart = models.ForeignKey(Cart,on_delete=models.CASCADE, null=True)
	complete = models.BooleanField(default=False)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	is_ordered = models.BooleanField(default=False)
	quantity = models.IntegerField(default=0)
	date_ordered = models.DateTimeField(auto_now=True)

	def get_cart_items(self):
		return self.orderitem_set.all()

	def get_cart_total(self):
		return sum([item.product.price * item.quantity for item in self.orderitem_set.all()])

	def __str__(self):
		return '{0} - {1}'.format(self.customer, self.ref_code)

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	quantity = models.IntegerField(default=0)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
	is_ordered = models.BooleanField(default=False)
	date_added = models.DateTimeField(auto_now=True)
	date_ordered = models.DateTimeField(null=True)

	def __str__(self):
		return f'{self.product.title} - {self.order}'
	
	def get_total(self):
		return self.quantity * self.product.price

class ShippingAddressCustomer(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.address} - {self.customer}'
class ShippingAddressOrder(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.address} - {self.order.ref_code}'