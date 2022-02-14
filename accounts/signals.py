from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.conf import settings
from shop.models import *
from .models import *


def profile(sender, instance, created, **kwargs):
	if created:
		if instance.is_vendor:
			group = Group.objects.get(name='Vendor')
			instance.groups.add(group)
			user = str(instance.first_name  + " " +instance.last_name)
			Vendor.objects.create(user=instance,username=user, email=instance.email,firstname=instance.first_name,lastname=instance.last_name)
			print("Profile created!")
		else:
			group = Group.objects.get(name='Customer')
			instance.groups.add(group)
			user = str(instance.first_name  + " " +instance.last_name)
			Customer.objects.create(user=instance,username=user, email=instance.email,firstname=instance.first_name,lastname=instance.last_name)
			print("Profile created!")

post_save.connect(profile,sender=User,dispatch_uid="profile")



def createShop(sender, instance, created, **kwargs):
	if created:
		chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
		randomstr = ''.join((random.choice(chars)) for x in range(10))
		shopname ='vendor-{randomstring}'.format(randomstring= randomstr)
		Shop.objects.create(vendor=instance,shopname=shopname)
		id = Shop.objects.filter(shopname=shopname).get().id
		Vendor.objects.filter(username="Jim Powu").update(storename=id)
		print("Shop created!")

post_save.connect(createShop,sender=Vendor,dispatch_uid="createShop")