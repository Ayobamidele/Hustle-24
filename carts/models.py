from datetime import datetime
from django.utils.translation import gettext_lazy as _
from accounts.models import Customer, Vendor
from django.db import models
from shop.models import Product

now = datetime.now() # current date and time
year = int(now.strftime("%Y"))+24


class CartItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
	quantity = models.IntegerField(default=0)
	ref_code = models.CharField(max_length=200, null=True)
	is_ordered = models.BooleanField(default=False)
	created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
	date_ordered = models.DateTimeField(null=True)
	date_delivered = models.DateTimeField(null=True)
	delivered = models.BooleanField(default=False)

	def __str__(self):
		return f'{self.product.title} - {self.cart}'
	
	def get_total_price(self):
		return self.quantity * self.product.price

class Cart(models.Model):
	customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
	ref_code = models.CharField(max_length=200, null=True)
	quantity = models.IntegerField(default=0)
	delivered = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
	updated = models.DateTimeField(auto_now_add=False,auto_now=True)
	complete = models.BooleanField(default=False)
	active = models.BooleanField(default=True)

	def __str__(self):
		return f'{self.ref_code} - {self.customer}'

	def get_cart_items(self):
		return CartItem.objects.filter(ref_code=self.ref_code)

	def get_cart_items_total_quantity(self):
		return sum([item.quantity for item in self.get_cart_items()])

	def get_cart_total_price(self):
		return sum([item.get_total_price() for item in self.get_cart_items()])

	def get_ref_code(self):
		# Get current datetime and format it (You might have to adjust the timezone)
		current_datetime = now.strftime('%Y%m%d%H%M%S')
		# Get the total amount of orders
		carts_count = Cart.objects.count()
		# Get the last order stored in the db
		last_cart = Cart.objects.last()
		# Get the id of the last order stored, if there is no order in the db, save a 0
		id = 0 if carts_count < 1 else last_cart.id
		# Creates an order with the format that you wanted
		ref_code = f'#{current_datetime}{id+1}'
		return ref_code


