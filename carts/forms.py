from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *


class ShippingAddressCustomerForm(ModelForm):
	class Meta:
		model = ShippingAddressCustomer
		fields = '__all__'
		exclude = [ 'customer' , 'active']

	def __init__(self, *args, **kwargs):
		super(ShippingAddressCustomerForm, self).__init__(*args, **kwargs)
		placeholder="&#61447; Username"
		for field in self.fields.keys():
			self.fields[field].widget.attrs.update({'class': 'form-control'})

class ShippingAddressOrderForm(ModelForm):
	class Meta:
		model = ShippingAddressOrder
		fields = '__all__'
		exclude = [ 'customer', 'order']


class ShippingPaymentCustomerForm(ModelForm):
	class Meta:
		model = ShippingPaymentCustomer
		fields = '__all__'
		exclude = [ 'customer' ]

	def __init__(self, *args, **kwargs):
		super(ShippingPaymentCustomerForm, self).__init__(*args, **kwargs)
		self.fields['card_number'].widget.attrs.update({'inputmode': 'numeric'})
		self.fields['card_number'].widget.attrs.update({'type': 'number'})
		# self.fields['card_number'].widget.attrs.update({'pattern': '[0-9\s]{13,19}'})
		self.fields['card_number'].widget.attrs.update({'autocomplete': 'cc-number'})
		# self.fields['card_number'].widget.attrs.update({'maxlength': '19'})
		self.fields['card_number'].widget.attrs.update({'placeholder': 'xxxx xxxx xxxx xxxx'})
		
		for field in self.fields.keys():
			self.fields[field].widget.attrs.update({'class': 'form-control'})
			

class ShippingPaymentOrderForm(ModelForm):
	class Meta:
		model = ShippingAddressCustomer
		fields = '__all__'
		exclude = [ 'customer', 'order' ]