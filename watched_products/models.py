from accounts.models import Customer
from django.db import models
from shop.models import Product
from django.utils.translation import gettext_lazy as _


class WatchList(models.Model):
	customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True, related_name="+")
	created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
	updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

	def __str__(self):
		return f"{self.customer} | {self.date_created} | {self.id}"


class WatchedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    initial_price = models.DecimalField(decimal_places=2, max_digits=100)
    initial_quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True, editable=False)
	
    def __str__(self):
        return f"{self.product} - {self.date_added}"


