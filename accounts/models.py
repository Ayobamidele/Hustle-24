from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	is_customer = models.BooleanField(default=True)
	is_vendor = models.BooleanField(default=False)


class Customer(models.Model):
	GENDER = (
			('Male', 'male'),
			('Female', 'female')
			)
	firstname = models.CharField(max_length=200, null=False)
	lastname = models.CharField(max_length=200, null=False)
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	username = models.CharField(max_length=200, null=False)
	phone_number = models.CharField(max_length=20)
	email = models.CharField(max_length=200, null=False)
	profile_pic = models.ImageField(null=True, blank=True)
	gender = models.CharField(max_length=200, null=True, choices=GENDER)
	
	def __str__(self):
		return str(self.firstname + " " + self.lastname)

class Vendor(models.Model):
	GENDER = (
			('Male', 'male'),
			('Female', 'female')
			)
	firstname = models.CharField(max_length=200, null=False)
	lastname = models.CharField(max_length=200, null=False)
	user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	username = models.CharField(max_length=200, null=False)
	phone_number = models.CharField(max_length=20)
	email = models.CharField(max_length=200, null=False)
	profile_pic = models.ImageField(null=True, blank=True)
	gender = models.CharField(max_length=200, null=True, choices=GENDER)
	is_vendor = models.BooleanField(default=True)
	
	def __str__(self):
		return str(self.firstname + " " + self.lastname)