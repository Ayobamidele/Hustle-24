import json
from .models import *
import random
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
	items = []
	order = {'get_cart_total': 0, 'get_cart_items': 0,'shipping': False}
	cartItems = order['get_cart_items']
	for i in cart:
		try:
			cartItems += cart[i]['quantity']
			product = Product.objects.get(id=i)
			total = (product.price * cart[i]['quantity'])
			order['get_cart_total'] += total
			order['get_cart_items'] += cart[i]['quantity']

			item = {
				'product':{
					'id': product.id,
					'title': product.title,
					'price': product.price,
					'image': product.image,
					},
				'quantity': cart[i]['quantity'],
				'get_total': total,
				}
			items.append(item)
		except:
			pass
	return {'items': items , 'order': order, 'cartItems':cartItems}

def cartData(request):
	if request.user.is_authenticated and request.user.is_customer == True:
		customer = request.user.customer
		print("was here",customer, request.user.is_customer)
		# the mess is here
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
		cartItems = order.quantity
		print(cartItems,order,"cartData")
	else:
		cookieData = cookieCart(request)
		cartItems = cookieData['cartItems']
		order = cookieData['order']
		items = cookieData['items']
	return {'items': items , 'order': order, 'cartItems':cartItems}

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
	
	