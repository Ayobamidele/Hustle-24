from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

GENDER = (
			('Male', 'male'),
			('Female', 'female')
			)
class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = [ 'user' ]
	
	def __init__(self, *args, **kwargs):
		super(CustomerForm, self).__init__(*args, **kwargs)
		for field in self.fields.keys():
			self.fields[field].widget.attrs.update({'class': 'form-control'})

class VendorForm(ModelForm):
	class Meta:
		model = Vendor
		fields = '__all__'
		exclude = [ 'user' ]
	
	def __init__(self, *args, **kwargs):
		super(VendorForm, self).__init__(*args, **kwargs)
		for field in self.fields.keys():
			self.fields[field].widget.attrs.update({'class': 'form-control'})

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email' , 'password1' , 'password2']
	
	def __init__(self, *args, **kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)
		for field in self.fields.keys():
			self.fields[field].widget.attrs.update({'class': 'form-control'})


class ChangeUserPasswordForm(UserCreationForm):
	class Meta:
		model = User
		# fields = '__all__'
		fields = ['password1' , 'password2']
	
	def __init__(self, *args, **kwargs):
		super(ChangeUserPasswordForm, self).__init__(*args, **kwargs)
		# self.fields['password1'].widget.attrs.update({'placeholder': 'New Password'})
		# self.fields['password2'].widget.attrs.update({'placeholder': 'Re-type New Password'})
		for field in self.fields.keys():
			self.fields[field].widget.attrs.update({'class': 'form-control'})