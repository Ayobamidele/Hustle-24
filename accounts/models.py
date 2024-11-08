import os
import random
from ast import arg

from django.contrib.auth.models import AbstractUser, Group, User, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
# from watched_products.models import watch_list

# Create your models here.

GENDER = (
			('Male', 'male'),
			('Female', 'female')
			)

class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_customer=True,
            is_vendor=False
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_active=True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)



class User(AbstractUser):
	is_customer = models.BooleanField(default=True)
	is_vendor = models.BooleanField(default=False)
	email = models.EmailField(_('email address'), unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']
	objects = MyAccountManager()

	def __str__(self):
		return str(self.email)

	def has_perm(self, perm, obj=None):
		return self.is_superuser

	def has_module_perms(self, app_label):
		return self.is_superuser


def photo_path(self, filename):	
	basefilename, file_extension= os.path.splitext(filename)
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
	randomstr = ''.join((random.choice(chars)) for x in range(10))
	return 'profileimages/{basename}{randomstring}{ext}'.format( basename= basefilename, randomstring= randomstr, ext= file_extension)

class Customer(models.Model):
	firstname = models.CharField(max_length=200, null=False)
	lastname = models.CharField(max_length=200, null=False)
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	username = models.CharField(max_length=200, null=False)
	phone_number = models.CharField(max_length=20)
	email = models.CharField(max_length=200, null=False)
	profile_pic = models.ImageField(upload_to=photo_path,default="victor-aldabalde-HguvvRqNgxo-unsplash.jpg")
	gender = models.CharField(max_length=200, null=True, choices=GENDER)
	watch_list = models.ManyToManyField(to="watched_products.WatchList", related_name="+")
	
	def __str__(self):
		return self.username

class Vendor(models.Model):
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

class AnonymousUsers(models.Model):
	email = models.EmailField(max_length=254,)
	date_created = models.DateTimeField(auto_now_add=True, null=True)


class WatchGroup(models.Model):
	members = models.ManyToManyField(to="User", related_name="members")
	watch_list = models.ManyToManyField(to="watched_products.WatchList", related_name="+")


class WatchGroupMember(models.Model):
	user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
	Group = models.OneToOneField(WatchGroup, on_delete=models.CASCADE, null=False, related_name="group")
	products_added = models.IntegerField(default=0)
	can_add = models.BooleanField(default=False)