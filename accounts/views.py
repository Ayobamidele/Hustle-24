from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import *
from .decorators import *
from shop.models import *
import json
from carts.models import *
from carts.forms import *
from carts.utils import cookieCart, cartData, guestOrder
from django.contrib.auth import get_user_model
User = get_user_model()

@unauthenticated_user
@with_usertype(allowed_roles=['Vendor'])
def registerPageCustomer(request):
	form = CreateUserForm()
	if request.method == "POST":
		print(request.POST)
		post = request.POST.copy() # to make it mutable
		post.update({'username': str(post['first_name'] + " " + post['last_name'])})
		form = CreateUserForm(post)
		if form.is_valid():
			# or set several values from dict
			print(post)
			print(form)
			username = post['first_name'] + " " + post['last_name']
			new_user = User.objects.create_user(username= username,
												email=post['email'],
												password=post['password1'],
												first_name=post['first_name'],
												last_name = post['last_name']
												)
			new_user.save()
			messages.success(request, 'Account was created for ' + username)
			return redirect('login')
	context = {'form': form}
	return render(request, 'accounts/register_customer.html', context)

@with_usertype(allowed_roles=['Customer'])
def registerPageVendor(request):
	form = CreateUserForm()
	if request.method == "POST":
		print(request.POST)
		post = request.POST.copy() # to make it mutable
		post.update({'username': str(post['first_name'] + " " + post['last_name'])})
		form = CreateUserForm(post)
		if form.is_valid():
			# or set several values from dict
			print(post)
			print(form)
			username = post['first_name'] + " " + post['last_name']
			new_user = User.objects.create_user(username= username,
												email=post['email'],
												password=post['password1'],
												first_name=post['first_name'],
												last_name=post['last_name'],
												is_vendor=True,
												is_customer=False,
												)
			new_user.save()
			messages.success(request, 'Account and Shop was created for ' + username)
			return redirect('login')
	context = {'form': form}
	return render(request, 'accounts/register_vendor.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')
		customer = request.POST.get('customer')
		user = authenticate(request, username=username, password=password)
		if user is not None:
			print('here1')
			if customer == "True":
				print('here2')
				if user.is_customer:
					try:
						cart = json.loads(request.COOKIES['cart'])
						customer = Customer.objects.get(user=user)
						order, created = Order.objects.get_or_create(customer=customer, complete=False)
						print(order)
						print(cart)
						cookieData = cookieCart(request)
						items = cookieData['items']
						for item in items:
							productitem = Product.objects.get(id=item['product']['id'])
							print('here3')
							print(productitem,item['quantity'])
							# oI= OrderItem.objects.create(order=cusorder,product=product,quantity=item['quantity'],is_ordered=True,)
							orderI=OrderItem.objects.create(
															order=order, 
															product=productitem, 
															quantity=item['quantity'], 
														)
							order.quantity += 1
							order.save()
							print('here4')
							orderI.save()
						request.COOKIES['cart'].clear()
					except:
						cart = {}
					login(request,user)
					return redirect(f'/customer/{username}',)
				else:
					messages.info(request, 'Username OR password is incorrect')
			else:
				print('here2')
				if user.is_vendor:
					login(request,user)
					print('here3')
					return redirect(f'/vendor/{username}',)
				else:
					messages.info(request, 'Username OR password is incorrect')
		else:
			messages.info(request, 'Username OR password is incorrect')					
	return render(request,'accounts/login.html')



def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def customerPage(request,customer):
	customer = request.user.customer
	userPicture = request.user
	orders = []
	orders1 = Order.objects.filter(customer=customer)
	for order in orders1:
		orderItems1 = order.orderitem_set.all()
		order1 = { 'order':  
								{
									'id' : order.ref_code,
									'orderItems' : [] ,
									'is_ordered' : order.is_ordered,
									'quantity' : order.quantity,
								}
				}
		for items in orderItems1:
			order1.get('order').get('orderItems').append(items)
		orders.append(order1)
	orders.reverse()
	if request.user.is_authenticated:
		if request.user.is_customer:
			userPicture = request.user.customer
		elif request.user.is_vendor:
			userPicture = request.user.vendor
	form = CustomerForm(instance=customer)
	passwordChangeForm = ChangeUserPasswordForm(instance=request.user)
	ShippingAddressForm = ShippingAddressCustomerForm(instance=request.user)
	ShippingPaymentForm = ShippingPaymentCustomerForm(instance=request.user)
	username = (f"{str(form.instance.firstname)} {str(form.instance.lastname)}").title()
	if request.method == "POST":
		form = CustomerForm(request.POST, request.FILES, instance=customer)
		print("Got here")

		if request.POST.get("form_type") == 'accountSetting':
            #Handle Elements from first Form
			if form.is_valid():
				print('valid')
				print(request.POST.get('form_type'))
				form.save()
		elif request.POST.get("form_type") == 'passwordChange':
			print(request.POST)
			# u = User.objects.get(username=form.instance.username)
			# if passwordChangeForm.is_valid():
				# passwordChangeForm.save()
				# print("password",request.POST,u)
	else:
		form = CustomerForm(instance=request.user.customer)
		passwordChangeForm = ChangeUserPasswordForm(instance=request.user)
		ShippingAddressForm = ShippingAddressCustomerForm(instance=request.user)
		ShippingPaymentForm = ShippingPaymentCustomerForm(instance=request.user)
	context = {	"customer": customer,
				"form": form,
				"passwordChangeForm": passwordChangeForm,
				"username": username,
				"userPicture": userPicture,
				"orders": orders,
				"totalOrders": len(orders),
				"ShippingPaymentForm": ShippingPaymentForm,
				"ShippingAddressForm": ShippingAddressForm,
			  }
	return render(request,'accounts/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Vendor'])
def vendorPage(request,vendor):
	vendor = request.user.vendor
	userPicture = request.user
	if request.user.is_authenticated:
		if request.user.is_customer:
			userPicture = request.user.customer
		elif request.user.is_vendor:
			userPicture = request.user.vendor
	shop = Shop.objects.get(vendor=vendor).shopname
	form = VendorForm(instance=vendor)
	if request.method == "POST":
		form = CustomerForm(request.POST, request.FILES, instance=vendor)
		if form.is_valid():
			form.save()
	context = {	"vendor": vendor, "form": form,'store': shop,"userPicture": userPicture}
	return render(request,'accounts/vendor.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request,'accounts/account_settings.html',context)