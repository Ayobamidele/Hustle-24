from .models import *
from accounts.models import *
from carts.utils import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from carts.models import *
import locale
import re
import json

# Create your views here.
from django.contrib.auth import get_user_model
from .decorators import *
from .forms import *

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

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['Vendor'])
# def shop(request,shop):
# 	userPicture = request.user
# 	if request.user.is_authenticated:
# 		if request.user.is_customer:
# 			userPicture = request.user.customer
# 		elif request.user.is_vendor:
# 			userPicture = request.user.vendor
# 			# print(userPicture.profile_pic.url)
# 	vendor = request.user.vendor
# 	store = Vendor.objects.filter(id=vendor.id).get().storename
# 	products = Shop.objects.filter(shopname=store).get().products.all()
# 	reviews = Shop.objects.filter(shopname=store).get().review.all()
# 	context = {'products':products,'store': store, 'reviews':reviews, 'userPicture': userPicture}
# 	return render(request,'shop/shop.html',context)

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

def addProduct(request,shop):
	form = AddProductForm()
	vendor = request.user.vendor
	products = Shop.objects.get(vendor=vendor.id).products.all()
	shop = Shop.objects.get(vendor=vendor)
	print(shop.products.all())
	productsId = [ product.id for product in products]
	reviews = []
	for x in productsId:
		z = ProductReview.objects.filter(product=x)
		for a in z:
			reviews.append(a)
	# print(shop.products)
	if request.method == "POST" and request.POST.get("form_type") == 'addProduct':
		title = request.POST.get('title')
		categories = request.POST.getlist('categories')
		brand = request.POST.get('brand')
		description = request.POST.get('description')
		stock =request.POST.get('stock')
		price = float((request.POST.get('price')[1:]).replace(',',''))
		discount = float((request.POST.get('discount')[1:]).replace(',',''))	
		image = request.FILES.get('choose-file')
		productImages = request.FILES.getlist('productImages')
		create_product = Product.objects.create(
				title=title,
				brand=brand,
				description=description,
				price=price,
				discount_price=discount,
				image=image,
				available=True,
				stock=stock,
				is_featured=True
			)
		for category in categories:
			# Check if string is empty or contain spaces only
			if not re.search("^\s*$", category):
				category_slug = category.replace(" ", "-")
				create_category = Category.objects.create(name=category,slug=category_slug)
				create_category.save()
				create_product.category.add(create_category)
		for image in productImages:
			create_ProductImage = ProductImage.objects.create(images=image)
			create_ProductImage.save()
			create_product.productimages.add(create_ProductImage)
		create_product.save()
		shop.products.add(create_product)
		shop.save()
	context = {'form': form,}
	return render(request,'shop/product-add.html',context)


def editProduct(request,shop,product,id):
	product = Product.objects.get(id=int(id))
	form = AddProductForm(instance=product)
	productimage = product.image.url
	productimages= product.productimages.all()
	categories = []
	for category in product.category.all():
		categories.append(category.name)
	for x in productimages:
		print(x.images.url)
	# vendor = request.user.vendor
	# products = Shop.objects.get(vendor=vendor.id).products.all()
	# shop = Shop.objects.get(vendor=vendor)
	# print(shop.products.all())
	# productsId = [ product.id for product in products]
	# reviews = []
	# for x in productsId:
	# 	z = ProductReview.objects.filter(product=x)
	# 	for a in z:
	# 		reviews.append(a)
	# # print(shop.products)
	if request.method == "POST" and request.POST.get("form_type") == 'addProduct':
		print(request.FILES)
	elif request.method == "POST":
		print(request.POST)
	# 	title = request.POST.get('title')
	# 	categories = request.POST.getlist('categories')
	# 	brand = request.POST.get('brand')
	# 	description = request.POST.get('description')
	# 	stock =request.POST.get('stock')
	# 	price = float((request.POST.get('price')[1:]).replace(',',''))
	# 	discount = float((request.POST.get('discount')[1:]).replace(',',''))	
	# 	image = request.FILES.get('choose-file')
	# 	productImages = request.FILES.getlist('productImages')
	# 	create_product = Product.objects.create(
	# 			title=title,
	# 			brand=brand,
	# 			description=description,
	# 			price=price,
	# 			discount_price=discount,
	# 			image=image,
	# 			available=True,
	# 			stock=stock,
	# 			is_featured=True
	# 		)
	# 	for category in categories:
	# 		# Check if string is empty or contain spaces only
	# 		if not re.search("^\s*$", category):
	# 			category_slug = category.replace(" ", "-")
	# 			create_category = Category.objects.create(name=category,slug=category_slug)
	# 			create_category.save()
	# 			create_product.category.add(create_category)
	# 	for image in productImages:
	# 		create_ProductImage = ProductImage.objects.create(images=image)
	# 		create_ProductImage.save()
	# 		create_product.productimages.add(create_ProductImage)
	# 	create_product.save()
	# 	shop.products.add(create_product)
	# 	shop.save()
	context = {'form': form,'id': id, 'productimage': productimage,
				'categories': categories,'productimages': productimages,}
	return render(request,'shop/product-edit.html',context)

def deleteProductImage(request):
	# data = json.loads(request.body)
	# print(data)
	print("got here",request.POST['motif'])
	return JsonResponse(status=302 ,data={'success' : request.POST['motif'] })