import datetime
import json
import os
import random

from accounts.forms import *
from accounts.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .decorators import *
from .models import *
from .utils import cartData, cookieCart, guestOrder
from .cart import Cart
from .forms import CartAddProductForm




User = get_user_model()



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

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	
	print('Action:', action)
	print('Product:', productId)
	
	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
		order.quantity = (order.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)
		order.quantity = (order.quantity - 1)
	orderItem.save()
	order.save()
	if action == 'removeAll':
		order.quantity = (order.quantity - orderItem.quantity)
		orderItem.delete()
		order.save()
	if orderItem.quantity <= 0:
		orderItem.delete()
	return JsonResponse('Item was added', safe=False)


@require_POST
def addItem(request):
	cart = Cart(request)
	product_id = int(request.POST.get("id"))
	product = get_object_or_404(Product, id=product_id)
	proposed_update = cart.cart[str(product_id)]['quantity'] + 1
	updated_request = request.POST.copy()
	updated_request.update({'quantity': proposed_update, "product": product})
	form = CartAddProductForm(updated_request)
	print(form.errors.as_json())
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
			messages.warning(request,"Product max quantity available")
    # max quantity available 
    # min quantity - Shey you dey wine me ni
	cartqty = cart.__len__()
	response = JsonResponse({"qty": cartqty, "Success": True})
	return response


@require_POST
def status(request):
	cart = Cart(request)
	cartqty = cart.__len__()
	response = JsonResponse({"qty": cartqty, "Success": True})
	return response


def checkout(request):
	userPicture = request.user
	if request.user.is_authenticated:
		if request.user.is_customer:
			userPicture = request.user.customer
		elif request.user.is_vendor:
			userPicture = request.user.vendor
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
				'regform': form,
				'userPicture': userPicture
			}
	return render(request, 'carts/checkout.html', context)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	if request.user.is_authenticated:
		customer = request.user.customer
		cusorder, created = Order.objects.get_or_create(complete=False,customer=customer)
		cusorder.complete=True
		cusorder.is_ordered=True
		cusorder.ref_code=generateRefCode()
		orderIdv = cusorder.ref_code
		cusorder.save()
		orderItems = cusorder.orderitem_set.all()
		for orderItem in orderItems:
			orderItem.is_ordered=True
			orderItem.save()
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']
		userData = json.loads(request.body)['form']
		print(cookieCart)
		print(cartItems)
		print(order)
		print(items)
		print(userData)
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
											last_name=userData['last_name']
											)
		new_user.save()
		messages.success(request, 'Account was created for ' + username)
		print(new_user.id)
		customer = Customer.objects.get(user=new_user.id)
		print("here")
		cusorder = Order.objects.create(
											customer=customer,
											complete=True,
											is_ordered=True,
											quantity=order['get_cart_items'],
											ref_code=generateRefCode()
											)
		print('here2')
		cusorder.save()
		orderIdv = cusorder.ref_code
		print(cusorder)
		for item in items:
			productitem = Product.objects.get(id=item['product']['id'])
			print('here3')
			print(productitem,cusorder,item['quantity'])
			orderI=OrderItem.objects.create(
											order=cusorder, 
											product=productitem, 
											quantity=item['quantity'], 
											is_ordered=True,
										)
			print('here4')
			orderI.save()
		"""
	Pass in order
	Get a order
	Get all vendors involved
	Arrange the order by vendor Id
	"""
	order = cusorder
	print(order)
	orderItems = order.get_cart_items()
	print(orderItems)
	allVendors = []
	allVendorsId = set([])
	sortedAllVendors = {}
	print(allVendors,allVendorsId,sortedAllVendors)
	for orderItem in orderItems:
		vendorId = orderItem.product.shop_set.first().vendor_id
		allVendorsId.add(vendorId)
		allVendors.append({ vendorId : [orderItem] })
	print("point 1")
	for id in allVendorsId:
		sortedAllVendors[id] = []
	print("point 2")
	def addOrder(orderId):
		for order in allVendors:
			if orderId in order.keys():
				for x in order[orderId]:
					sortedAllVendors[orderId].append(x)
	print("point 3")
	for order in allVendorsId:
		addOrder(order)
	print("point 4")
	for cartkey in sortedAllVendors:
		vendorUser = Vendor.objects.get(id=cartkey)
		vendorsCart = Cart.objects.create()
		vendorsCart.vendor = vendorUser
		print(vendorsCart.vendor)
		vendorsCart.order = cusorder
		print("point 5",vendorsCart)
		for orderedProducts in sortedAllVendors[cartkey]:
			vendorsCart.totalprice += orderedProducts.get_total()
			print(vendorsCart.totalprice)
			productitem = Product.objects.get(id=orderedProducts.product.id)
			vendorsCart.products.add(productitem)
			orderedProduct = CartItem.objects.create(
											cart=vendorsCart, 
											product=productitem, 
											quantity=orderedProducts.quantity, 
											is_ordered=True,
										)
			orderedProduct.save()
			vendorsCart.quantity += orderedProducts.quantity
			print("point 6")
		print("point 7",vendorsCart)
		vendorsCart.save()
		print("point 8")
	return JsonResponse('Payment complete!', safe=False)
