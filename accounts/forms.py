from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate, login, logout
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
		exclude = [ 'user', 'orders' ]
	
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

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user