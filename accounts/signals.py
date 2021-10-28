from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.conf import settings
from .models import Customer


def customer_profile(sender, instance, created, **kwargs):
	if created:
		group = Group.objects.get(name='Customer')
		instance.groups.add(group)
		user = str(instance.first_name  + " " +instance.last_name)
		Customer.objects.create(user=instance,username=user, email=instance.email,firstname=instance.first_name,lastname=instance.last_name)
		print("Profile created!")

post_save.connect(customer_profile,sender=settings.AUTH_USER_MODEL,dispatch_uid="customer_profile")