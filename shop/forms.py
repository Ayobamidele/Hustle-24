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
		self.fields['stock'].widget.attrs.update({'type': 'number',
			'onkeypress': 'return isNumberKey(event)', 'min': 1})
		for field in self.fields.keys():
			self.fields[field].widget.attrs.update({'class': 'form-control'})
			print(field)
		self.fields['description'].widget.attrs['class'] = 'form-control textarea'
		self.fields['price'].widget.attrs.update({'type': 'price',
			'placeholder': 'Type a number & click outside', 'min': 0.00,
			'onkeypress': 'return isNumberKey(event)'})