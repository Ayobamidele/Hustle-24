from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .decorators import *
from .models import *
from .utils import cookieCart, cartData

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
import datetime
import random
import json
import os
from accounts.models import *
from accounts.forms import *
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.


def generateRefCode():	
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
	randomstr = ''.join((random.choice(chars)) for x in range(10))
	return randomstr


def cart(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'carts/cart.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	
	print('Action:', action)
	print('Product:', productId)
	
	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	print("came here")
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
		order.quantity = (order.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
		order.quantity = (order.quantity - 1)
	orderItem.save()
	order.save()
	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def checkout(request):
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	if request.user.is_authenticated:
		display_register = False
		form = CreateUserForm()
	else:
		display_register = True
		form = CreateUserForm()
	context = {'items':items, 'order':order,
				'cartItems':cartItems,
				'display_register':display_register,
				'regform': form
			}
	return render(request, 'carts/checkout.html', context)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer,complete=True)
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']
		userData = json.loads(request.body)['form']
		print('total')
		print(items)
		# Create user
		print(userData)
		username = userData['first_name'] + " " + userData['last_name']
		password = userData['password']
		print(username ,password)
		new_user = User.objects.create_user(username= username,
											email=userData['email'],
											password=password,
											first_name=userData['first_name'],
											last_name = userData['last_name']
											)
		new_user.save()
		messages.success(request, 'Account was created for ' + username)
		print(new_user.id)
		customer = Customer.objects.get(user=new_user.id)
		print("here")
		cusorder= Order.objects.create(
											customer=customer,
											complete=True,
											is_ordered=True,
											quantity=order['get_cart_items'],
											ref_code=generateRefCode()
											)
		print('here2')
		cusorder.save()
		print(cusorder)
		for item in items:
			productitem = Product.objects.get(id=item['product']['id'])
			print('here3')
			print(productitem,cusorder,item['quantity'])
			# oI= OrderItem.objects.create(order=cusorder,product=product,quantity=item['quantity'],is_ordered=True,)
			orderI=OrderItem.objects.create(
											order=cusorder, 
											product=productitem, 
											quantity=item['quantity'], 
											is_ordered=True,
										)
			print('here4')
			orderI.save()
		# pass in order


		# customer, order = guestOrder (request, data)
		# total = float(data['form']['total'])
		# order, transaction_id - transaction_id
		# if total == float(order.get_cart_total):
		# 	order.complete = True
		# 	order.save()
	return JsonResponse ('Payment complete!', safe=False)
