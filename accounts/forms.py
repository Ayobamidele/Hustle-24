from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = [ 'user' ]

class VendorForm(ModelForm):
	class Meta:
		model = Vendor
		fields = '__all__'
		exclude = [ 'user' ]

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email' , 'password1' , 'password2']
