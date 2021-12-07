from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class ShippingAddressCustomerForm(ModelForm):
	class Meta:
		model = ShippingAddressCustomer
		fields = '__all__'
		exclude = [ 'customer' ]

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
		for field in self.fields.keys():
			self.fields[field].widget.attrs.update({'class': 'form-control'})
			

class ShippingPaymentOrderForm(ModelForm):
	class Meta:
		model = ShippingAddressCustomer
		fields = '__all__'
		exclude = [ 'customer', 'order' ]