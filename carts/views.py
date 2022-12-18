import datetime
import json
import os
import random

from accounts.forms import *
from accounts.models import *
from orders.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST, require_GET

from .decorators import *
from .models import *
from .utils import cartData, cookieCart, guestOrder
from .cart import Cart
from .forms import CartAddProductForm



User = get_user_model()

@require_GET
def send_messages(request):
	storage = messages.get_messages(request)
	storage.used = True
	stringed_messages = [str(item) for item in storage._loaded_messages]
	
	response = JsonResponse({"messages": stringed_messages, "Success": True})

	return response


def generateRefCode():	
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
	randomstr = ''.join((random.choice(chars)) for x in range(10))
	return randomstr

def cart(request):
	userPicture = 'user.png'
	if request.user.is_authenticated:
		if request.user.is_customer:
			userPicture = request.user.customer.profile_pic.url
		elif request.user.is_vendor:
			userPicture = request.user.vendor.profile_pic.url
	cart = Cart(request)
	cart_items = cart
	# print(dir(cart_items.cart),cart_items.cart.get('2'))
	total_items = cart.__len__()
	total_price = cart.get_total_price
	context = { 'total_price': total_price,'userPicture':userPicture,
				'cart_items':cart_items, 'total_items': total_items,
			  }
	return render(request, 'carts/cart.html', context)


@require_POST
def addItem(request):
	cart = Cart(request)
	product_id = int(request.POST.get("id"))
	product = get_object_or_404(Product, id=product_id)
	if cart.cart != {}:
		if str(product_id) not in cart.cart.keys():
			proposed_update = 1
		else:
			proposed_update = cart.cart[str(product_id)]['quantity'] + 1
		updated_request = request.POST.copy()
		updated_request.update({'quantity': proposed_update, "product": product})
		form = CartAddProductForm(updated_request)
	else:
		updated_request = request.POST.copy()
		updated_request.update({'quantity': 1, "product": product})
		form = CartAddProductForm(updated_request)
	# print(form.errors.as_json(),form.errors,dir(form))
	if form.is_valid():
		cd = form.cleaned_data
		cart.add(product=product,
				quantity=cd['quantity'],
				update_quantity=True
				)
	else:
		if "product" in form.errors.as_json():
			messages.warning(request,"Product doesn't exists")
		elif "Quantity":
			messages.add_message(request, messages.INFO, "You have maxed the quantity available for this product")
    # max quantity available 
    # min quantity - Shey you dey wine me ni
	cartqty = cart.__len__()
	total_price = f"{(cart.cart[str(product_id)]['quantity'] * product.regular_price):n}" if type(cart.cart[str(product_id)]['quantity']) == int else False
	updated_quantity = cart.cart[str(product_id)]['quantity'] if type(cart.cart[str(product_id)]['quantity']) == int else False
	response = JsonResponse({"qty": cartqty, "prc": f"{cart.get_total_price():n}", "Success": True, "total_price": total_price, "updated_quantity": updated_quantity })
	return response


@require_POST
def removeItem(request):
	cart = Cart(request)
	removeItem = False
	product_id = int(request.POST.get("id"))
	product = get_object_or_404(Product, id=product_id)
	if str(product_id) in cart.cart.keys():
		item = cart.cart[str(product_id)]['quantity']
		if item > 1:
			proposed_update = cart.cart[str(product_id)]['quantity'] - 1
			updated_request = request.POST.copy()
			updated_request.update({'quantity': proposed_update, "product": product})
			form = CartAddProductForm(updated_request)
			if form.is_valid():
				cd = form.cleaned_data
				cart.minus(product=product,
							quantity=cd['quantity'],)
			else:
				messages.add_message(request, messages.WARNING, "Error with quantity being removed!!!")
		else:
			cart.remove(product)
			removeItem = True
			print(cart.cart)
	cartqty = cart.__len__()
	try:
		total_price = f"{(cart.cart[str(product_id)]['quantity'] * product.regular_price):n}" if type(cart.cart[str(product_id)]['quantity']) == int else False
		updated_quantity = cart.cart[str(product_id)]['quantity'] if type(cart.cart[str(product_id)]['quantity']) == int else False
	except Exception as e:
		total_price = False
		updated_quantity = False
	response = JsonResponse({"qty": cartqty, "prc": f"{cart.get_total_price():n}", "removeItem": removeItem, "Success": True, "total_price": total_price, "updated_quantity": updated_quantity })
	return response


@require_POST
def removeAllItems(request):
	cart = Cart(request)
	product_id = int(request.POST.get("id"))
	product = get_object_or_404(Product, id=product_id)
	if str(product_id) in cart.cart.keys():
		cart.remove(product)
	cartqty = cart.__len__()
	response = JsonResponse({"qty": cartqty, "prc": f"{cart.get_total_price():n}", "Success": True })
	return response



@require_POST
def status(request):
	cart = Cart(request)
	cartqty = cart.__len__()
	response = JsonResponse({"qty": cartqty, "Success": True})
	return response


def checkout_authentication(request):
	if request.method == "POST":
		print(request.POST)
		form = AnonymousUserForm(request.POST)
		if form.is_valid():
			AnonymousUsers.objects.create(email=request.POST.get('email'))
			return redirect('carts:checkout_location')
	else:
		userPicture = 'user.png'
		if request.user.is_authenticated:
			if request.user.is_customer:
				userPicture = request.user.customer
			elif request.user.is_vendor:
				userPicture = request.user.vendor
		cart = Cart(request)
		cart_items = cart
		form = AnonymousUserForm()
		print(form)
		display_register = False if request.user.is_authenticated else True
		shipping = { "cost": 25, }
		order = { "discount": 0, "cost": sum( [shipping['cost'] , cart.get_total_price(),]) , "complete": True }
	context = {
				'cart_items':cart_items,
				'display_register':display_register,
				'form': form,
				'shipping': shipping,
				'order': order,
				'userPicture': userPicture
			}
	return render(request, 'carts/checkout/checkout_authentication.html', context)

def checkout_location(request):
	if request.method == "POST":
		print(request.POST)
	else:
		userPicture = 'user.png'
		if request.user.is_authenticated:
			if request.user.is_customer:
				userPicture = request.user.customer
			elif request.user.is_vendor:
				userPicture = request.user.vendor
		cart = Cart(request)
		cart_items = cart
		form = ShippingAddressForm()
		print(form)
		display_register = False if request.user.is_authenticated else True
		shipping = { "cost": 25, }
		order = { "discount": 0, "cost": sum( [shipping['cost'] , cart.get_total_price(),]) , "complete": True }
	context = {
				'cart_items':cart_items,
				'display_register':display_register,
				'form': form,
				'shipping': shipping,
				'order': order,
				'userPicture': userPicture
			}
	return render(request, 'carts/checkout/checkout_shipping.html', context)




@require_POST
def processOrder(request):
	if request.user.is_authenticated:
		print("Got Here Authenticated!")
		# customer = request.user.customer
		# cusorder, created = Order.objects.get_or_create(complete=False,customer=customer)
		# cusorder.complete = True
		# cusorder.is_ordered = True
		# cusorder.ref_code = generateRefCode()
		# orderIdv = cusorder.ref_code
		# cusorder.save()
		# orderItems = cusorder.orderitem_set.all()
		# for orderItem in orderItems:
		# 	orderItem.is_ordered=True
		# 	orderItem.save()
	else:
		print("Got Here Unauthenticated!")
		# 1. Get form data, user info, delivery, payment
		# 2. Get cart data
		# 3. Create anonymous user account
		# 4. Create Order for the vendor's item
		# 5. Process Payment




	# 	cookieData = cookieCart(request)
	# 	cartItems = cookieData['cartItems']
	# 	order = cookieData['order']
	# 	items = cookieData['items']
	# 	userData = json.loads(request.body)['form']
	# 	print(cookieCart)
	# 	print(cartItems)
	# 	print(order)
	# 	print(items)
	# 	print(userData)
	# 	print(items)
	# 	# Create user
	# 	print(userData)
	# 	username = userData['first_name'] + " " + userData['last_name']
	# 	password = userData['password']
	# 	print(username ,password)
	# 	new_user = User.objects.create_user(username= username,
	# 										email=userData['email'],
	# 										password=password,
	# 										first_name=userData['first_name'],
	# 										last_name=userData['last_name']
	# 										)
	# 	new_user.save()
	# 	messages.success(request, 'Account was created for ' + username)
	# 	print(new_user.id)
	# 	customer = Customer.objects.get(user=new_user.id)
	# 	print("here")
	# 	cusorder = Order.objects.create(
	# 										customer=customer,
	# 										complete=True,
	# 										is_ordered=True,
	# 										quantity=order['get_cart_items'],
	# 										ref_code=generateRefCode()
	# 										)
	# 	print('here2')
	# 	cusorder.save()
	# 	orderIdv = cusorder.ref_code
	# 	print(cusorder)
	# 	for item in items:
	# 		productitem = Product.objects.get(id=item['product']['id'])
	# 		print('here3')
	# 		print(productitem,cusorder,item['quantity'])
	# 		orderI=OrderItem.objects.create(
	# 										order=cusorder, 
	# 										product=productitem, 
	# 										quantity=item['quantity'], 
	# 										is_ordered=True,
	# 									)
	# 		print('here4')
	# 		orderI.save()
	# 	"""
	# Pass in order
	# Get a order
	# Get all vendors involved
	# Arrange the order by vendor Id
	# """
	# order = cusorder
	# print(order)
	# orderItems = order.get_cart_items()
	# print(orderItems)
	# allVendors = []
	# allVendorsId = set([])
	# sortedAllVendors = {}
	# print(allVendors,allVendorsId,sortedAllVendors)
	# for orderItem in orderItems:
	# 	vendorId = orderItem.product.shop_set.first().vendor_id
	# 	allVendorsId.add(vendorId)
	# 	allVendors.append({ vendorId : [orderItem] })
	# print("point 1")
	# for id in allVendorsId:
	# 	sortedAllVendors[id] = []
	# print("point 2")
	# def addOrder(orderId):
	# 	for order in allVendors:
	# 		if orderId in order.keys():
	# 			for x in order[orderId]:
	# 				sortedAllVendors[orderId].append(x)
	# print("point 3")
	# for order in allVendorsId:
	# 	addOrder(order)
	# print("point 4")
	# for cartkey in sortedAllVendors:
	# 	vendorUser = Vendor.objects.get(id=cartkey)
	# 	vendorsCart = Cart.objects.create()
	# 	vendorsCart.vendor = vendorUser
	# 	print(vendorsCart.vendor)
	# 	vendorsCart.order = cusorder
	# 	print("point 5",vendorsCart)
	# 	for orderedProducts in sortedAllVendors[cartkey]:
	# 		vendorsCart.totalprice += orderedProducts.get_total()
	# 		print(vendorsCart.totalprice)
	# 		productitem = Product.objects.get(id=orderedProducts.product.id)
	# 		vendorsCart.products.add(productitem)
	# 		orderedProduct = CartItem.objects.create(
	# 										cart=vendorsCart, 
	# 										product=productitem, 
	# 										quantity=orderedProducts.quantity, 
	# 										is_ordered=True,
	# 									)
	# 		orderedProduct.save()
	# 		vendorsCart.quantity += orderedProducts.quantity
	# 		print("point 6")
	# 	print("point 7",vendorsCart)
	# 	vendorsCart.save()
	# 	print("point 8")
	return JsonResponse('Payment complete!', safe=False)



