from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class AddProductForm(ModelForm):
	class Meta:
		model = Product
		fields = '__all__'

	def __init__(self, *args, **kwargs):
		super(AddProductForm, self).__init__(*args, **kwargs)		
		for field in self.fields.keys():
			self.fields[field].widget.attrs.update({'class': 'form-control'})
			print(field)