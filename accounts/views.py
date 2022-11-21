import datetime
import json
from orders.forms import *
from carts.models import *
from carts.utils import *
from django.contrib import messages
from django.contrib.auth import (authenticate, get_user_model, login, logout,
                                 update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from shop.models import *
from orders.models import *
from .decorators import *
from .forms import *
from .models import *
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import views as auth_views
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
# from django.contrib.auth.models import User
from django.conf import settings
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes




User = get_user_model()
Now = datetime.now()


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "accounts/password/password_reset_email.txt"
					c = {
					"email": user.email,
					'domain': get_current_site(request),
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, settings.EMAIL_HOST_USER , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect("password_reset/done/")
			else:
				messages.warning(request, 'Email does not exist!')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="accounts/password/password_reset.html", context={"password_reset_form":password_reset_form})



@unauthenticated_user
@with_usertype(allowed_roles=['Vendor','bami'])
def registerCustomer(request):
	form = CreateUserForm()
	if request.method == "POST":
		form = CreateUserForm(request.POST)
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password1')
		password_confirmation = request.POST.get('password2')
		print("Hello, ",request.POST,request.POST.get('password'), form.is_valid())
		if password == password_confirmation:			
			new_user = User.objects.create_user(username=username,password=password,email=email,)
			new_user.save()
			messages.success(request, 'Account was created for ' + username)
			return redirect('accounts:login')
	context = {'form': form}
	return render(request, 'accounts/index.html', context)

@with_usertype(allowed_roles=['Customer'])
def registerVendor(request):
	if request.user.is_anonymous:
		return redirect('accounts:login')
	else:
		if request.user.is_customer and request.user.is_vendor == False:
			user = User.objects.get(id=request.user.id)
			user.is_vendor = True
			user.save()
			Vendor.objects.create(
				user=request.user,
				username=request.user.username,
				email=request.user.email,
				firstname=request.user.first_name,
				lastname=request.user.last_name
			)
			return redirect(f'/vendor/{request.user.username}')
		else:
			form = CreateUserForm()
			if request.method == "POST":
				firstname = request.POST.get('firstname')
				lastname = request.POST.get('lastname')
				email = request.POST.get('email')
				password = request.POST.get('password')
				print("Hello, ",request.POST,request.POST.get('password'))
				if password:			
					username = firstname + " " + lastname
					new_user = User.objects.create_user(username= username,
														email=email,
														password=password,
														first_name=firstname,
														last_name = lastname,
														is_vendor=True,
														)
					new_user.save()
					messages.success(request,'Account and Shop was created for ' + username)
					return redirect('accounts:login')
			context = {'form': form}
	return render(request, 'accounts/register_vendor.html', context)

@unauthenticated_user
def loginPage(request):
	form = AccountAuthenticationForm(request.POST or None)
	if request.POST:
		email = request.POST.get('email')
		password = request.POST.get('password')
		if form.is_valid():
			user =  authenticate(email=email, password=password)
			print('here1', user.username)
			# try:
			# 	cart = json.loads(request.COOKIES['cart'])
			# 	customer = Customer.objects.get(user=user)
			# 	order, created = Order.objects.get_or_create(customer=customer, complete=False)
			# 	print(order)
			# 	print(cart)
			# 	cookieData = cookieCart(request)
			# 	items = cookieData['items']
			# 	for item in items:
			# 		productitem = Product.objects.get(id=item['product']['id'])
			# 		print('here3')
			# 		print(productitem,item['quantity'])
			# 		# oI= OrderItem.objects.create(order=cusorder,product=product,quantity=item['quantity'],is_ordered=True,)
			# 		orderI=OrderItem.objects.create(
			# 										order=order, 
			# 										product=productitem, 
			# 										quantity=item['quantity'], 
			# 									)
			# 		order.quantity += 1
			# 		order.save()
			# 		print('here4')
			# 		orderI.save()
			# 	request.COOKIES['cart'].clear()
			# except:
			# 	cart = {}
			if user:
				login(request, user)
				messages.success(request, "Logged In")
				print('hopefully')
				return redirect(f'/customer/{email}',)
			# elif user.is_vendor:
			# 	login(request,user)
			# 	print('here3')
			# 	return redirect(f'/vendor/{username}',)
		else:
			messages.info(request, 'Username OR password is incorrect')				
	return render(request,'accounts/signin.html', {'form': form })
	
def logoutUser(request):
    logout(request)
    return redirect('accounts:login')
# vendor/bami
@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['Customer'])
def customerPage(request,customer):
	customer = request.user.customer
	vendor = request.user.vendor if request.user.is_vendor else ""
	carts = []
	data = cartData(request)
	cart_data = data['cart_data']
	cart_items = data['cart_items']
	customerAddresses = ShippingAddress.objects.filter(customer=customer)
	customerPayments = ShippingPayment.objects.filter(customer=customer)
	customerCarts = Cart.objects.filter(customer=customer)
	# print(customerPayments)
	# for payments in customerPayments:
	# 	print(payments.name_on_card)
	for cart in customerCarts:
		cart_details = {'cart':
								{
									'ref_code': cart.ref_code,
									'cart_items': cart.get_cart_items(),
									'is_ordered': cart.complete,
									'quantity': cart.quantity,
									'get_cart_items_total_quantity': cart.get_cart_items_total_quantity(),
									'get_cart_total_price': cart.get_cart_total_price(),
								}
						}
		carts.append(cart_details)
	carts.reverse()
	userPicture = request.user.customer.profile_pic.url
	customerForm = CustomerForm(instance=customer)
	passwordChangeForm = ChangeUserPasswordForm(instance=request.user)
	shippingAddressForm = ShippingAddressForm(instance=customer)
	shippingPaymentForm = ShippingPaymentForm()
	pictureForm = ChangePictureForm()
	username = (f"{customer.firstname} {customer.lastname}").title()
	username = username if bool(username.strip()) else customer.username
	print(request.POST,"Customer Page",  request.POST.get("form_type"),request.FILES)
	if request.method == "POST" and request.POST.get("form_type") == 'accountSetting':
		customerForm = CustomerForm(request.POST, request.FILES, instance=customer)
		if customerForm.is_valid():
			customerForm.save()
		if request.user.is_vendor:
			vendorForm = VendorForm(request.POST, request.FILES, instance=vendor)
			if vendorForm.is_valid():
				vendorForm.save()
	elif request.method == "POST" and request.POST.get("form_type") == 'passwordChange':
		passwordChangeForm = ChangeUserPasswordForm(request.POST, request.FILES,instance=request.user)
		if passwordChangeForm.is_valid():
			passwordChangeForm.save()
			update_session_auth_hash(request, request.user)
	elif request.method == "POST" and request.POST.get("form_type") == 'AddressAdded':
		shippingAddressForm = ShippingAddressForm(request.POST, request.FILES,instance=customer)
		print(ShippingAddressForm,request.POST)
		if shippingAddressForm.is_valid():
			print("erere")
			for address in customerAddresses:
				address.active = False
				address.save()
			new_address = ShippingAddress()
			new_address.customer = customer
			new_address.address = ShippingAddressForm.cleaned_data['address']
			new_address.city = ShippingAddressForm.cleaned_data['city']
			new_address.state = ShippingAddressForm.cleaned_data['state']
			new_address.zipcode = ShippingAddressForm.cleaned_data['zipcode']
			new_address.active = True
			new_address.save()
			print(new_address)
	elif request.method == "POST" and request.POST.get("form_type") == 'PaymentAdded':
		shippingPaymentForm = ShippingPaymentForm(request.POST, request.FILES,instance=customer)
		if shippingPaymentForm.is_valid():
			print("ererepayment")
			if customerPayments.exists():
				for payment in customerPayments:
					payment.active = False
					payment.save()
			new_payment = ShippingPayment()
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
		deactivePayment = ShippingPayment.objects.get(id=int(request.POST.get("paymentId")))
		deactivePayment.active = True
		deactivePayment.save()
		print("Payment Activated!!!")
	elif request.method == "POST" and request.POST.get("form_type") == 'ActivateAddress':
		for address in customerAddresses:
			address.active = False
			address.save()
		deactiveAddress = ShippingAddress.objects.get(id=int(request.POST.get("addressId")))
		deactiveAddress.active = True
		deactiveAddress.save()
		print("Address Activated!!!")
	elif request.method == "POST" and request.POST.get("form_type") == 'profilePicutureSetting':
		print("Ready for Upload")
		pictureForm = ChangePictureForm(request.POST, request.FILES,instance=customer)
		if pictureForm.is_valid():
			pictureForm.save()
			update_session_auth_hash(request, request.user)
		return JsonResponse( {	"message": "Image Uploaded",})
	context = {	"customer": customer,
				"customerForm": customerForm,
				"passwordChangeForm": passwordChangeForm,
				"username": username,
				"userPicture": userPicture,
				"carts": carts,
				'cart_data': cart_data,
				"totalCarts": len(carts),
				"totalAddress": len(customerAddresses),
				"totalPayments": len(customerPayments),
				"ShippingPaymentForm": ShippingPaymentForm,
				"ShippingAddressForm": ShippingAddressForm,
				"customerAddress" : customerAddresses,
				"customerPayments": customerPayments,
				"cartItems": cart_items,
				"pictureForm": pictureForm,
			  }
	return render(request,'accounts/customer.html',context)

@login_required(login_url='accounts:login')
@allowed_users(allowed_roles=['Vendor','Customer'])
def vendorPage(request,vendor):
	vendor = request.user.vendor
	userPicture = request.user
	# orders = OrderItem.objects.all()
	products = Shop.objects.get(vendor=vendor.id).products.all()
	productsId = [ product.id for product in products]
	reviews = []
	data = cartData(request)
	cart_items = data['cart_items']
	for x in productsId:
		z = ProductReview.objects.filter(product=x)
		for a in z:
			reviews.append(a)
	order_list = set([])
	deliveredcarts = Order.objects.filter(vendor=vendor.id)
	allorderedcarts = Order.objects.filter(vendor=vendor.id)
	undeliveredcarts = Order.objects.filter(vendor=vendor.id)
	userPicture = request.user.customer.profile_pic.url
	shop = Shop.objects.get(vendor=vendor).shopname
	form = VendorForm(instance=vendor)
	passwordChangeForm = ChangeUserPasswordForm(instance=request.user)
	username = (f"{str(form.instance.firstname)} {str(form.instance.lastname)}").title()
	if request.method == "POST" and request.POST.get("form_type") == 'itemDelivered':
		item = CartItem.objects.get(id=int(request.POST.get('order-number')))
		item.delivered = True
		# item.date_ordered = Now
		item.save()
	elif request.method == "POST" and request.POST.get("form_type") == 'DeliveredAll':
		deliveredOrder = Cart.objects.get(id=int(request.POST.get('order-number')))
		for cartItem in deliveredOrder.get_cart_items():
			if not cartItem.delivered:
				cartItem.delivered = True
				cartItem.save()
		deliveredOrder.completely_delivered = True
		deliveredOrder.save()
	context = {	"vendor": vendor, "form": form,
				'store': shop,"userPicture": userPicture,
				"username": username,"passwordChangeForm": passwordChangeForm,
				"carts" : undeliveredcarts, "cart_total" : "make it js",
				"allCarts": allorderedcarts, "deliveredcarts": deliveredcarts,
				"products": products, "cartItems": cart_items,
	}
	return render(request,'accounts/vendor.html',context)

@login_required(login_url='accounts:login')
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
	