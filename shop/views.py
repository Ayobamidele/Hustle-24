from django.shortcuts import render
from .models import *
from accounts.models import *
from django.shortcuts import get_object_or_404

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

import locale

# Create your views here.
from django.contrib.auth import get_user_model
from .decorators import *

locale.setlocale(locale.LC_ALL, '')

def home(request,category_slug=None):
	category = None
	user = request.user
	userId = request.user.id
	products = Product.objects.filter(available=True)
	categories = Category.objects.all()
	# if category_slug:
	# 	category = get_object_or_404(Category, slug=category_slug)
	# 	products = products.fiter(category=category)
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
		description = product.description
		link = str(title)
		image = product.image.url
		productsdict.append({'title': title,'price': price,'description': description,'link': link, 'image': image})
	print(productsdict)
	# for product in productsdict:
	context = { 'productsdict':productsdict,
				'show': show,
				'id': userId,
				"user": user,
				}
	
	return render(request, 'shop/index.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Vendor'])
def shop(request,shop):
	vendor = request.user.vendor
	store = Vendor.objects.filter(id=vendor.id).get().storename
	products = Shop.objects.filter(shopname=store).get().products.all()
	reviews = Shop.objects.filter(shopname=store).get().review.all()
	context = {'products':products,'store': store, 'reviews':reviews}
	return render(request,'shop/shop.html',context)

def productDetail(request,product):
	product = Product.objects.filter(title=product).get()
	store = product.shop_set.get()
	price = f'{product.price:n}'
	images = product.productimages.all()
	mainimage = product.image.url
	productsdict = []
	print(product.description)
	for image in images.all():
		productsdict.append({'image': str('images/' + str(image))})
	context = {'product': product,'price': price, 'store': store, 'productsdict': productsdict, 'mainimage': mainimage}
	return render(request,'shop/product.html',context)