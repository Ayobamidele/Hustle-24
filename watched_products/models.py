from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.forms import ValidationError

# Create your models here.

class WatchList(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	group = models.ForeignKey(to="accounts.WatchGroup", on_delete=models.CASCADE, null=True,related_name="+")
	customer = models.ForeignKey(to="accounts.Customer", on_delete=models.CASCADE, null=True, related_name="+")
	product =  models.ForeignKey(to="shop.WatchedProduct", on_delete=models.CASCADE, null=True, related_name="+")
	date_created = models.DateTimeField(auto_now_add=True)
	content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,null=True)
	object_id = models.PositiveIntegerField(null=True)
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return f"{self.date_added}|{self.id}"

	def clean(self):
		"""Ensure that only one of `price_euro` and `price_dollars` can be set."""
		if self.group and self.customer:
			raise ValidationError("Only one price field can be set.")

	class Meta:
		constraints = [
			models.CheckConstraint(
				check=(
					Q(group__isnull=False) & 
					Q(customer__isnull=True)
				) | (
					Q(group__isnull=True) & 
					Q(customer__isnull=False)
				),
				name='only_one_price',
			)
		]
