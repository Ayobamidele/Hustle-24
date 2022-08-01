import json

from django.http import HttpResponse, JsonResponse
from shop.models import *


def cookiewatchlist(request):
	try:
		watchlist = json.loads(request.COOKIES['watchlist'])
	except:
		watchlist = {}
	items = {}
	for i in watchlist:
		try:
			product = Product.objects.get(id=i)
			item = {
					'id': product.id,
					'title': product.title,
					'price': product.price,
					'image': product.image,
					'date': watchlist[i]['date'],
					'quantity': watchlist[i]['quantity'],
				}
			items[product.id] = item
		except:
			pass
	return JsonResponse({'success': True,}, status=200)