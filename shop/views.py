import ast
import json
import locale
import re
from dis import dis

from accounts.models import *
from carts.models import *
from carts.utils import *
# Create your views here.
from django.contrib.auth import get_user_model
# from django.forms import inlineformset_factory
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import authenticate, login, logout
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
# from permissions import *
# from rest_framework import renderers, viewsets
# from rest_framework.response import Response

from .decorators import *
from .forms import *
from .models import *

locale.setlocale(locale.LC_ALL, '')
deletedProductImages = set([])


def generate_ref_code():
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
	random_str = ''.join((random.choice(chars)) for _ in range(10))
	return random_str


def home(request, category_slug=None):
	userPicture = 'user.png'
	if request.user.is_authenticated:
		if request.user.is_customer:
			userPicture = request.user.customer.profile_pic.url
		elif request.user.is_vendor:
			userPicture = request.user.vendor.profile_pic.url
	user = request.user
	userId = request.user.id
	ref_code = generateRefCode
	# products = Product.objects.filter(is_active=True)
	products = Product.objects.prefetch_related("image").filter(is_active=True)
	data = cartData(request)
	cart_data = data['cart_data']
	cart_items = data['cart_items']
	# print(cart_data.ref_code,1111)
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
		price = product.regular_price
		pid = product.id
		description = product.description
		link = product.get_absolute_url
		image = product.image.first().image.url
		productsdict.append({'title': title, 'price': price,
							'description': description, 'link': link, 'image': image, 'id': pid})
	context = {'data': productsdict,
			   'show': show,
			   'id': userId,
			   'user': user,
			   'cart_data': cart_data,
			   'userPicture': userPicture
			   }
	return render(request, 'shop/index.html', context)


def productDetail(request, title,ref_code,shop):
	userPicture = 'user.png'
	if request.user.is_authenticated:
		if request.user.is_customer:
			userPicture = request.user.customer.profile_pic.url
		elif request.user.is_vendor:
			userPicture = request.user.vendor.profile_pic.url
	product = Product.objects.filter(ref_code=ref_code).get()
	store = product.get_shop
	price = f'{product.regular_price:n}'
	images = product.image.filter(is_feature=True).all()
	mainimage = product.image.filter(is_feature=False).first().image.url
	productsdict = []
	print(product.get_shop.vendor_id, Shop.objects.get(id=store.id).products.all())
	data = cartData(request)
	cart_data = data['cart_data']
	cart_items = data['cart_items']
	for image in images.all():
		productsdict.append({'image': str('images/' + str(image))})
	context = {'userPicture': userPicture, 'product': product, 'price': price, 'store': store,
			   'productsdict': productsdict, 'mainimage': mainimage, 'cartItems': cart_items, }
	return render(request, 'shop/product.html', context)


# @unauthenticated_user
@login_required(login_url='login')
@with_usertype(allowed_roles=['Vendor'])
def addProduct(request, shop):
	form = AddProductForm()
	vendor = request.user.vendor
	products = Shop.objects.get(vendor=vendor.id).products.all()
	shop = Shop.objects.get(vendor=vendor)
	print(shop.products.all())
	productsId = [product.id for product in products]
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
		stock = request.POST.get('stock')
		price = float((request.POST.get('price')[1:]).replace(',', ''))
		discount = float((request.POST.get('discount')[1:]).replace(',', ''))
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
				create_category = Category.objects.create(
					name=category, slug=category_slug)
				create_category.save()
				create_product.category.add(create_category)
		for image in productImages:
			create_ProductImage = ProductImage.objects.create(images=image)
			create_ProductImage.save()
			create_product.productimages.add(create_ProductImage)
		create_product.save()
		shop.products.add(create_product)
		shop.save()
	context = {'form': form, }
	return render(request, 'shop/product-add.html', context)


# @unauthenticated_user
@login_required(login_url='login')
@with_usertype(allowed_roles=['Vendor'])
def editProduct(request, shop, product, id):
	product = Product.objects.get(id=int(id))
	form = AddProductForm(instance=product)
	productimage = product.image.url
	productimages = product.productimages.all()
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
	if request.method == "POST" and request.POST.get("form_type") == 'editProduct':
		# print(request.POST, deletedProductImages,22222333)
		title = request.POST.get('title')
		categoriesRecieved = request.POST.getlist('categories')
		brand = request.POST.get('brand')
		description = request.POST.get('description')
		stock = request.POST.get('stock')
		# Price
		price = request.POST.get('price')
		non_decimalPrice = re.compile(r'[^\d.]+')
		price = float(non_decimalPrice.sub('', price))
		# Discount
		discount = request.POST.get('discount')
		print(discount)
		non_decimalDiscount = re.compile(r'[^\d.]+')
		discount = float(non_decimalDiscount.sub('', discount))

		image = request.FILES.get('choose-file')
		productImages = request.FILES.getlist('productImages')

		print(title, categories, brand, description,
			  stock, price, discount, image, productImages)
		product.title = title
		product.brand = brand
		product.description = description
		product.price = price
		product.discount = discount

		if image == None:
			pass
		else:
			product.image = image
	# for itemCategory in categoriesRecieved:
	# 	if itemCategory in categories:
	# 		pass
	# 	else

	# for imageItem in deletedProductImages:
	# 	productExtraImage

	# for category in categories:
	# 	# Check if string is empty or contain spaces only
	# 	if not re.search("^\s*$", category):
	# 		category_slug = category.replace(" ", "-")
	# 		create_category = Category.objects.create(name=category,slug=category_slug)
	# 		create_category.save()
	# 		create_product.category.add(create_category)
	# create_product = Product.objects.create(
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
	deletedProductImages.clear()
	context = {'form': form, 'id': id, 'productimage': productimage,
			   'categories': categories, 'productimages': productimages, }
	return render(request, 'shop/product-edit.html', context)


# @unauthenticated_user
@login_required(login_url='login')
@with_usertype(allowed_roles=['Vendor'])
def deleteProductImage(request):
	data = request.POST['motif']
	data = ast.literal_eval(data)
	for x in data:
		deletedProductImages.add(x)
	return JsonResponse({'success': True}, status=200)
