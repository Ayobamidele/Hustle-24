from .models import *
from accounts.models import *
from carts.utils import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from carts.models import *
import locale

# Create your views here.
from django.contrib.auth import get_user_model
from .decorators import *

locale.setlocale(locale.LC_ALL, '')

def generateRefCode():	
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
	randomstr = ''.join((random.choice(chars)) for x in range(10))
	return randomstr


def home(request,category_slug=None):
	userPicture = request.user
	if request.user.is_authenticated:
		if request.user.is_customer:
			userPicture = request.user.customer
		elif request.user.is_vendor:
			userPicture = request.user.vendor
	user = request.user
	userId = request.user.id
	ref_code = generateRefCode
	# print(ref_code, r)
	products = Product.objects.filter(available=True)
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	show = True
	for group in request.user.groups.all():
		print(group)
		if 'Vendor' == str(group):
			show = False
	# print(products.productimages)
	# products = list(products)
	productsdict = []
	for product in products:
		title = product.title
		price = product.price
		pid = product.id
		description = product.description
		link = str(title)
		image = product.image.url
		productsdict.append({'title': title,'price': price,'description': description,'link': link, 'image': image, 'id': pid})
	# print(productsdict,cartItems)
	# for product in productsdict:
	print(cartItems)
	context = { 'productsdict':productsdict,
				'show': show,
				'id': userId,
				'user': user,
				'cartItems':cartItems,
				'userPicture': userPicture
				}
	return render(request, 'shop/index.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Vendor'])
def shop(request,shop):
	userPicture = request.user
	if request.user.is_authenticated:
		if request.user.is_customer:
			userPicture = request.user.customer
		elif request.user.is_vendor:
			userPicture = request.user.vendor
			print(userPicture.profile_pic.url)
	vendor = request.user.vendor
	store = Vendor.objects.filter(id=vendor.id).get().storename
	products = Shop.objects.filter(shopname=store).get().products.all()
	reviews = Shop.objects.filter(shopname=store).get().review.all()
	context = {'products':products,'store': store, 'reviews':reviews, 'userPicture': userPicture}
	return render(request,'shop/shop.html',context)

def productDetail(request,product):
	userPicture = request.user
	if request.user.is_authenticated:
		if request.user.is_customer:
			userPicture = request.user.customer
		elif request.user.is_vendor:
			userPicture = request.user.vendor
	product = Product.objects.filter(title=product).get()
	store = product.shop_set.get()
	price = f'{product.price:n}'
	images = product.productimages.all()
	mainimage = product.image.url
	productsdict = []
	print(product.description)
	data = cartData(request)
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']
	for image in images.all():
		productsdict.append({'image': str('images/' + str(image))})
	context = {'userPicture': userPicture,'product': product,'price': price, 'store': store, 'productsdict': productsdict, 'mainimage': mainimage, 'cartItems':cartItems,}
	return render(request,'shop/product.html',context)