from django.shortcuts import render
from .models import *
from accounts.models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
# Create your views here.

def home(request,category_slug=None):
	category = None
	customerId = request.user.id
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
	print(show)
	context = { 'products':products,
				'show': show,
				'id': customerId,
				}
	return render(request, 'shop/store.html', context)

