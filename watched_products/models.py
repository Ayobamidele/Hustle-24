from accounts.models import Customer
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from django.forms import ValidationError
from shop.models import WatchedProduct

# Create your models here.

class WatchList(models.Model):
	title = models.CharField(max_length=255, null=True, blank=True)
	# This feature is under construction
	# group = models.ForeignKey(to="accounts.WatchGroup", on_delete=models.CASCADE, null=True,related_name="+")
	
	customer = models.OneToOneField(Customer, on_delete=models.CASCADE, null=True, related_name="+")
	products =  models.ManyToManyField(WatchedProduct, related_name="+")
	date_created = models.DateTimeField(auto_now_add=True)
	# content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,null=True)
	# object_id = models.PositiveIntegerField(null=True)
	# content_object = GenericForeignKey('content_type', 'customer')
	# editable = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.customer} | {self.date_created} | {self.id}"

	# def clean(self):
	# 	"""Ensure that only one of `group` and `customer` can be set."""
	# 	if self.group and self.customer:
	# 		raise ValidationError("Only one owner field can be set.")

	# def save(self):
	# 	self.clean()
	# 	# if self.group:
	# 	# 	self.editable=True
	# 	# else:
	# 	# 	self.editable=False
		

	# class Meta:
	# 	constraints = [
	# 		models.CheckConstraint(
	# 			check=(
	# 				Q(group__isnull=False) & 
	# 				Q(customer__isnull=True)
	# 			) | (
	# 				Q(group__isnull=True) & 
	# 				Q(customer__isnull=False)
	# 			),
	# 			name='only_one_price',
	# 		)
	# 	]
