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
			elif user.is_vendor:
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
	customerAddresses = ShippingAddressCustomer.objects.filter(customer=customer)
	customerPayments = ShippingPaymentCustomer.objects.filter(customer=customer)
	print(customerPayments)
	for payments in customerPayments:
		print(payments.name_on_card)
	orders1 = Order.objects.filter(customer=customer)
	for order in orders1:
		orderItems1 = order.orderitem_set.all()
		order1 = { 'order':  
								{
									'id' : order.ref_code,
									'orderItems' : [] ,
									'is_ordered' : order.is_ordered,
									'quantity' : order.quantity,
									'get_cart_items' : order.quantity,
									'get_cart_total' : order.get_cart_total(),
								}
				}
		print(order1)
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
	ShippingAddressForm = ShippingAddressCustomerForm(instance=customer)
	ShippingPaymentForm = ShippingPaymentCustomerForm()
	username = (f"{str(form.instance.firstname)} {str(form.instance.lastname)}").title()
	print(request.POST)
	if request.method == "POST" and request.POST.get("form_type") == 'accountSetting':
		form = CustomerForm(request.POST, request.FILES, instance=customer)
		if form.is_valid():
			form.save()
	elif request.method == "POST" and request.POST.get("form_type") == 'passwordChange':
		passwordChangeForm = ChangeUserPasswordForm(request.POST, request.FILES,instance=request.user)
		if passwordChangeForm.is_valid():
			passwordChangeForm.save()
	elif request.method == "POST" and request.POST.get("form_type") == 'AddressAdded':
		ShippingAddressForm = ShippingAddressCustomerForm(request.POST, request.FILES,instance=customer)
		print(ShippingAddressForm,request.POST)
		if ShippingAddressForm.is_valid():
			print("erere")
			for address in customerAddresses:
				address.active = False
				address.save()
			new_address = ShippingAddressCustomer()
			new_address.customer = customer
			new_address.address = ShippingAddressForm.cleaned_data['address']
			new_address.city = ShippingAddressForm.cleaned_data['city']
			new_address.state = ShippingAddressForm.cleaned_data['state']
			new_address.zipcode = ShippingAddressForm.cleaned_data['zipcode']
			new_address.active = True
			new_address.save()
			print(new_address)
	elif request.method == "POST" and request.POST.get("form_type") == 'PaymentAdded':
		ShippingPaymentForm = ShippingPaymentCustomerForm(request.POST, request.FILES,instance=customer)
		if ShippingPaymentForm.is_valid():
			print("ererepayment")
			if customerPayments.exists():
				for payment in customerPayments:
					payment.active = False
					payment.save()
			new_payment = ShippingPaymentCustomer()
			new_payment.customer = customer
			new_payment.card_number = ShippingPaymentForm.cleaned_data['card_number']
			new_payment.name_on_card = ShippingPaymentForm.cleaned_data['name_on_card']
			new_payment.expiry_month = ShippingPaymentForm.cleaned_data['expiry_month']
			new_payment.expiry_year = ShippingPaymentForm.cleaned_data['expiry_year']
			new_payment.security_code = ShippingPaymentForm.cleaned_data['security_code']
			new_payment.active = True
			new_payment.save()
			print(new_payment)
	elif request.method == "POST" and request.POST.get("form_type") == 'ActivatePayment':
		for payment in customerPayments:
			payment.active = False
			payment.save()
		deactivePayment = ShippingPaymentCustomer.objects.get(id=int(request.POST.get("paymentId")))
		deactivePayment.active = True
		deactivePayment.save()
		print("Payment Activated!!!")
	elif request.method == "POST" and request.POST.get("form_type") == 'ActivateAddress':
		for address in customerAddresses:
			address.active = False
			address.save()
		deactiveAddress = ShippingAddressCustomer.objects.get(id=int(request.POST.get("addressId")))
		deactiveAddress.active = True
		deactiveAddress.save()
		print("Address Activated!!!")
	context = {	"customer": customer,
				"form": form,
				"passwordChangeForm": passwordChangeForm,
				"username": username,
				"userPicture": userPicture,
				"orders": orders,
				"totalOrders": len(orders),
				"totalAddress": len(customerAddresses),
				"totalPayments": len(customerPayments),
				"ShippingPaymentForm": ShippingPaymentForm,
				"ShippingAddressForm": ShippingAddressForm,
				"customerAddress" : customerAddresses,
				"customerPayments": customerPayments,
			  }
	return render(request,'accounts/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Vendor'])
def vendorPage(request,vendor):
	vendor = request.user.vendor
	userPicture = request.user
	orders = OrderItem.objects.all()
	products = Shop.objects.get(vendor=vendor.id).products.all()
	products = [ product.id for product in products]
	order_list = set([])
	"""
	Get a order
	Get all vendors involved
	Arrange the order by vendor Id
	"""
	order = Order.objects.get(ref_code="dRDn25iAwk")
	orderItems = order.get_cart_items()
	allVendors = []
	allVendorsId = set([])
	sortedAllVendors = {}
	for orderItem in orderItems:
		vendorId = orderItem.product.shop_set.first().vendor_id
		allVendorsId.add(vendorId)
		allVendors.append({vendorId : [orderItem] })
		allVendorsId.add(vendorId)
	for id in allVendorsId:
		sortedAllVendors[id] = []
	

	def addOrder(orderId):
		for order in allVendors:
			if orderId in order.keys():
				for x in order[orderId]:
					sortedAllVendors[orderId].append(x)
	# addOrder(14)
	for order in allVendorsId:
		addOrder(order)

	print(sortedAllVendors)
	# for order in orders:
	# 	if order.product.id in products:
	# 		orderId = order.order.id
	# 		order2 = Order.objects.get(id=orderId)
	# 		if order2.is_ordered :
	# 			order_list.add(order2)
	# 			order_details = {
	# 				"order": order2,
	# 				"quantity": order.quantity,
	# 				"get_total": order.get_total(),
	# 				"address": order2.address.address,
	# 				"city": order2.address.city,
	# 				"state": order2.address.state,
	# 				"zipcode": order2.address.zipcode,
	# 				"country": order2.address.country,
	# 				"card_number": order2.payment.card_number,
	# 				"email": order2.customer.email,
	# 				"phone_number": order2.customer.phone_number,
	# 				"name_on_card": order2.payment.name_on_card,
	# 			}
	# 			print(order_details)
	# print(order_list)
	# print(products)
	if request.user.is_authenticated:
		if request.user.is_customer:
			userPicture = request.user.customer
		elif request.user.is_vendor:
			userPicture = request.user.vendor
	shop = Shop.objects.get(vendor=vendor).shopname
	form = VendorForm(instance=vendor)
	passwordChangeForm = ChangeUserPasswordForm(instance=request.user)
	username = (f"{str(form.instance.firstname)} {str(form.instance.lastname)}").title()
	if request.method == "POST" and request.POST.get("form_type") == 'accountSetting':
		form = VendorForm(request.POST, request.FILES, instance=vendor)
		if form.is_valid():
			form.save()
	elif request.method == "POST" and request.POST.get("form_type") == 'passwordChange':
		passwordChangeForm = ChangeUserPasswordForm(request.POST, request.FILES,instance=request.user)
		if passwordChangeForm.is_valid():
			passwordChangeForm.save()
	context = {	"vendor": vendor, "form": form,'store': shop,"userPicture": userPicture,
				"username": username,
				"passwordChangeForm": passwordChangeForm,
	}
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