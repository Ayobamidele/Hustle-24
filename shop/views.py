from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request, category_slug=None):
	category = None
	products = Product.objects.filter(available=True)
	categories = Category.objects.all()
	# if category_slug:
	# 	category = get_object_or_404(Category, slug=category_slug)
	# 	products = products.fiter(category=category)
	context = {'products':products}
	return render(request, 'shop/store.html', context)

