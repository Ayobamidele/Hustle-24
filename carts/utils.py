import json
import random
from shop.models import *
from .models import *


def generateRefCode():	
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
	randomstr = ''.join((random.choice(chars)) for x in range(10))
	return randomstr


def cookieCart(request):
	try:
		cart = json.loads(request.COOKIES['cart'])
	except:
		cart = {}
		print('Cart:', cart)
	cart_items = []
	cart_data = {
		'cart_total_quantity': 0,
		'cart_items_quantity': 0,
		'shipping': False,
		'cart_total_price': 0,
		}

	for cart_item in cart:
		try:
			cart_data['cart_total_quantity'] += cart[cart_item]['quantity']
			product = Product.objects.get(id=cart_item)
			product_image = ProductImage.objects.filter(product=cart_item)
			total = (product.price * cart[cart_item]['quantity'])
			cart_data['cart_total_price'] += total
			cart_data['cart_items_quantitys'] += 1

			item = {
				'product':{
					'id': product.id,
					'title': product.title,
					'price': product.price,
					'image': product_image,
					},
				'quantity': cart[cart_item]['quantity'],
				'get_total': total,
				}
			
			cart_items.append(item)
		except:
			pass
	return {'cart_items': cart_items ,'cart_data': cart_data}

def cartData(request):
	if request.user.is_authenticated and request.user.is_customer == True:
		customer = request.user.customer
		print("was here",customer, request.user.is_customer)
		# the mess is here
		cart, created = Cart.objects.get_or_create(customer=customer, complete=False)
		cart.ref_code = cart.get_ref_code() if cart.ref_code == None else cart.ref_code
		print(11111222, cart.ref_code)
		cart_items = cart.get_cart_items()
		totalCartItems = cart.quantity
		cartTotalItems = cart_items.__len__()
		cart_data = cart
		# print(cartItems,order,"cartData")
	else:
		cookieData = cookieCart(request)
		cart_items = cookieData['cart_items']
		cart_data = cookieData['cart_data']
	return {'cart_items': cart_items, 'cart_data': cart_data}

def guestOrder(request, data):
	# collects user form data
	try:
		first_name = data['form']['first_name']
		last_name = data['form']['last_name']
		password = data['form']['password']
		email = data['form']['email']
		username = str(first_name) + " " + str(last_name)
	except :
		pass
	else:
		username = data['form']['username']
		password = data['form']['password']

	#Collects cart data
	cookieData = cookieCart(request)
	cartItems = cookieData['cartItems']
	order = cookieData['order']
	items = cookieData['items']

	# Create or Get Customer object
	try:
		customer, created = Customer.objects.get_or_create(
				email=email,
				first_name=first_name,
				last_name=last_name,
				username=username,
				password=password
		)
		customer.save()
	except:
		pass
	else:
		customer, created = Customer.objects.get_or_create(
				username=username,
				password=password
		)
	# Create the order for the customer
	order = Order.objects.create(
						customer=customer,
						complete=True,
						is_ordered=True,
						quantity=order['get_cart_items'],
						ref_code=generateRefCode()
	)
	#Create the order items
	for item in items:
		productitem = Product.objects.get(id=item['product']['id'])
		orderI=OrderItem.objects.create(
										order=order, 
										product=productitem, 
										quantity=item['quantity'], 
										is_ordered=True,
									)
		print('here4')
		orderI.save()
	return customer, order
	
	