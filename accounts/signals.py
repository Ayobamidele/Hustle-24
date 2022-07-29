from django.conf import settings
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from shop.models import *

from .models import *


def profile(sender, instance, created, **kwargs):
	if created:
		if instance.is_vendor and instance.is_customer:
			group = Group.objects.get_or_create(name='Vendor')
			instance.groups.add(group[0].id)
			group = Group.objects.get_or_create(name='Customer')
			instance.groups.add(group[0].id)
			user = str(instance.first_name  + " " +instance.last_name) if instance.user_name == None else instance.username
			Customer.objects.create(user=instance,username=user, email=instance.email,firstname=instance.first_name,lastname=instance.last_name)
			Vendor.objects.create(user=instance,username=user, email=instance.email,firstname=instance.first_name,lastname=instance.last_name)
			print("Profile created!")
		else:
			group = Group.objects.get_or_create(name='Customer')
			instance.groups.add(group[0].id)
			# user = str(instance.first_name  + " " +instance.last_name)
			user = str(instance.first_name  + " " +instance.last_name) if instance.username == None else instance.username
			Customer.objects.create(user=instance,username=user,
				email=instance.email,firstname=instance.first_name,lastname=instance.last_name)
			print("Profile created!")

post_save.connect(profile,sender=User,dispatch_uid="profile")



def createShop(sender, instance, created, **kwargs):
	if created:
		chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
		randomstr = ''.join((random.choice(chars)) for x in range(10))
		shopname ='vendor-{randomstring}'.format(randomstring= randomstr)
		Shop.objects.create(vendor=instance,shopname=shopname)
		print("Shop created!")
		id = Shop.objects.filter(shopname=shopname).get().id
		Vendor.objects.filter(username=instance.username).update(storename=id)

post_save.connect(createShop,sender=Vendor,dispatch_uid="createShop")