from ast import arg
from django.db import models
import os
import random
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group

# Create your models here.
class User(AbstractUser):
	is_customer = models.BooleanField(default=True)
	is_vendor = models.BooleanField(default=False)

def photo_path(self, filename):	
	basefilename, file_extension= os.path.splitext(filename)
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
	randomstr = ''.join((random.choice(chars)) for x in range(10))
	return 'profileimages/{basename}{randomstring}{ext}'.format( basename= basefilename, randomstring= randomstr, ext= file_extension)

class Customer(models.Model):
	GENDER = (
			('Male', 'male'),
			('Female', 'female')
			)
	firstname = models.CharField(max_length=200, null=False)
	lastname = models.CharField(max_length=200, null=False)
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	username = models.CharField(max_length=200, null=False)
	phone_number = models.CharField(max_length=20)
	email = models.CharField(max_length=200, null=False)
	profile_pic = models.ImageField(upload_to=photo_path,default="victor-aldabalde-HguvvRqNgxo-unsplash.jpg")
	gender = models.CharField(max_length=200, null=True, choices=GENDER)
	
	def __str__(self):
		return self.username

class Vendor(models.Model):
	GENDER = (
			('Male', 'male'),
			('Female', 'female')
			)
	firstname = models.CharField(max_length=200, null=False)
	lastname = models.CharField(max_length=200, null=False)
	storename = models.OneToOneField(related_name='+', to='shop.Shop', on_delete=models.CASCADE,blank=True, null=True)
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	username = models.CharField(max_length=200, null=False)
	phone_number = models.CharField(max_length=20)
	email = models.CharField(max_length=200, null=False)
	profile_pic = models.ImageField(null=True, blank=True,upload_to=photo_path,default='levi-stute-mFF39sOZSgM-unsplash.jpg')
	gender = models.CharField(max_length=200, null=True, choices=GENDER)
	orders = models.IntegerField(default=0)
	
	def __str__(self):
		return str(self.firstname + " " + self.lastname)