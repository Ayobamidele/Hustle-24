from datetime import datetime

from accounts.models import Customer, Vendor
from django.db import models
from shop.models import Product

now = datetime.now() # current date and time
year = int(now.strftime("%Y"))+24

# Create your models here.
class ShippingAddressOrder(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)
	country = models.CharField(max_length=200, null=False,default="")

	def __str__(self):
		return self.address

class ShippingPaymentOrder(models.Model):
	MONTH_CHOICES = [(i, i) for i in range(1, 12)]
	YEAR_CHOICES = [(i, i) for i in range(1919, year)]
	YEAR_CHOICES.reverse()
	
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	card_number= models.CharField(max_length=23, null=False)
	name_on_card= models.CharField(max_length=200, null=False)
	expiry_month= models.CharField(max_length=2, choices=MONTH_CHOICES, null=False)
	expiry_year= models.CharField(max_length=4, choices=YEAR_CHOICES, null=False)
	security_code= models.CharField(max_length=4, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.card_number} - {self.customer}'

class Order(models.Model):
	ref_code = models.CharField(max_length=200, null=True)
	address = models.ForeignKey(ShippingAddressOrder, on_delete=models.CASCADE, null=True)
	payment = models.ForeignKey(ShippingPaymentOrder, on_delete=models.CASCADE, null=True)
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
	date_added = models.DateTimeField(auto_now_add=True)
	date_ordered = models.DateTimeField(null=True)

	def __str__(self):
		return f'{self.product.title} - {self.order}'
	
	def get_total(self):
		return self.quantity * self.product.price

class Cart(models.Model):
	vendor = models.ForeignKey(to=Vendor ,on_delete=models.CASCADE, null=True)
	products = models.ManyToManyField(Product)
	totalprice = models.DecimalField(max_digits=10,decimal_places=2, default=0)
	quantity = models.IntegerField(default=0)
	completely_delivered = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	active = models.BooleanField(default=True)
	order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return f'{self.vendor}'
		# return f'{self.order.ref_code} - {self.vendor}'

	def get_cart_items(self):
		return self.cartitem_set.all()

	def get_cart_items_length(self):
		return len(self.get_cart_items())

	def get_cart_total(self):
		return sum([item.product.price * item.quantity for item in self.cartitem_set.all()])

class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	quantity = models.IntegerField(default=0)
	cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, null=True, blank=True)
	is_ordered = models.BooleanField(default=False)
	date_added = models.DateTimeField(auto_now_add=True)
	date_ordered = models.DateTimeField(null=True)
	delivered = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.product.title} - {self.cart}'
	
	def get_total(self):
		return self.quantity * self.product.price

class ShippingAddressCustomer(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)
	country = models.CharField(max_length=200, null=False,default="")

	def __str__(self):
		return f'{self.address} - {self.customer}'


class ShippingPaymentCustomer(models.Model):
	MONTH_CHOICES = [(i, i) for i in range(1, 12)]
	YEAR_CHOICES = [(i, i) for i in range(1919, year)]
	YEAR_CHOICES.reverse()

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	card_number= models.CharField(max_length=23, null=False)
	name_on_card = models.CharField(max_length=200, null=False)
	expiry_month = models.CharField(max_length=2,choices=MONTH_CHOICES, null=False)
	expiry_year = models.CharField(max_length=4, choices=YEAR_CHOICES, null=False)
	security_code = models.CharField(max_length=4, null=False)
	date_added = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.card_number} - {self.customer}'


