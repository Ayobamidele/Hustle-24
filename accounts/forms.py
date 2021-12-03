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
	firstname = forms.CharField(label='First Name',widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
	lastname = forms.CharField(label='Last Name',widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
	username = forms.CharField(label='User Name',widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
	email = forms.CharField(label='Email',widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
	phone_number = forms.CharField(label='Phone Number',widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
	gender = forms.ChoiceField(label='Gender', choices=GENDER,widget=forms.Select(attrs={'class': 'form-control'}),required=True)
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
