import json
from .models import *
from .utils import *


def update_watch_list(request):
	customer = request.user.customer
	data = json.loads(request.body)
	productId = int(data['productId'])
	action = data['action']
	product = Product.objects.get(id=productId)
	quantity = data['quantity']
	price = data['price']
	date = data['date']

	print('Action:', action)
	print('Product:', product)
	print('quantity', quantity)
	print('price:', price)
	print('date:', date)

	print(data)
	if action == 'add':
		watchedProduct, created = WatchedProduct.objects.get_or_create(
			initial_price=price,
			initial_quantity=quantity,
			product=product,
			)
		watchedProduct.save()
		watchList, created = WatchList.objects.get_or_create(
			title='Personal',
			customer=customer,
			)
		product = Product.objects.get(id=productId)
		watchList.products.add(watchedProduct)
		watchList.save()
	elif action == 'remove':
		watchList = WatchList.objects.get(customer=customer)
		watchedProducts = watchList.products.all()
		for item in watchedProducts:
			if item.product.id == productId:
				item.delete()
	if len(customer.watch_list.all()) < 1:
		customer.watch_list.add(watchList)
	return JsonResponse(f'Item was {{action}}', safe=False)
