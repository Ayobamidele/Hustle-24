from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

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
		self.fields['card_number'].widget.attrs.update({'placeholder': '&#\f1e6'})
		for field in self.fields.keys():
			self.fields[field].widget.attrs.update({'class': 'form-control'})
			

class ShippingPaymentOrderForm(ModelForm):
	class Meta:
		model = ShippingAddressCustomer
		fields = '__all__'
		exclude = [ 'customer', 'order' ]