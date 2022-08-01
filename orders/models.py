from django.db import models
from accounts.models import Customer, Vendor
from datetime import datetime
from shop.models import Product
from django.utils.translation import gettext_lazy as _

now = datetime.now() # current date and time
year = int(now.strftime("%Y"))+24

class ShippingAddress(models.Model):
	"""
	Shipping address details for customers orders.
	"""
	STATUS_CHOICES = (
		("In Use", "IN USE"),
		("DeLeted" ,"DELETED")
	)
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
	active = models.BooleanField(default=False)
	country = models.CharField(max_length=200, null=False,default="")
	ref_code = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=False, default=STATUS_CHOICES[0][0])

	def __str__(self):
		return f'{self.address} - {self.customer}'


class ShippingPayment(models.Model):
	"""
	Shipping payment details for customers orders.
	"""
	MONTH_CHOICES = [(i, i) for i in range(1, 12)]
	YEAR_CHOICES = [(i, i) for i in range(1919, year)]
	YEAR_CHOICES.reverse()
	STATUS_CHOICES = (
		("In Use", "IN USE"),
		("DeLeted" ,"DELETED")
	)

	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	card_number= models.CharField(max_length=23, null=False)
	name_on_card = models.CharField(max_length=200, null=False)
	expiry_month = models.CharField(max_length=2,choices=MONTH_CHOICES, null=False)
	expiry_year = models.CharField(max_length=4, choices=YEAR_CHOICES, null=False)
	security_code = models.CharField(max_length=4, null=False)
	ref_code = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=False, default=STATUS_CHOICES[0][0])
	created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
	active = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.card_number} - {self.customer}'



class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	quantity = models.IntegerField(default=0)
	ref_code = models.CharField(max_length=200, null=True)
	is_ordered = models.BooleanField(default=False)
	created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
	date_ordered = models.DateTimeField(null=True)
	date_delivered = models.DateTimeField(null=True)
	delivered = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.product.title} - {self.ref_code}'
	
	def get_total_price(self):
		return self.quantity * self.product.price


class Order(models.Model):
	ref_code = models.CharField(max_length=200, null=True)
	complete = models.BooleanField(default=False)
	vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=True)
	is_ordered = models.BooleanField(default=False)
	quantity = models.IntegerField(default=0)
	date_ordered = models.DateTimeField(auto_now=True)

	def get_address(self):
		return ShippingAddress.objects.filter(ref_code=self.ref_code).first()

	def get_payment(self):
		return ShippingPayment.objects.filter(ref_code=self.ref_code).first()

	def get_order_items(self):
		return OrderItem.objects.filter(ref_code=self.ref_code)

	def get_order_total(self):
		return sum([item.get_total_price() for item in self.orderitem_set.all()])

	def __str__(self):
		return f'{self.customer} - {self.ref_code}'

