from django import template
from django.templatetags.static import static
from watched_products.utils import cookiewatchlist

# Create your models here.

register = template.Library()

# @register.filter


@register.simple_tag
def check_user_wishlist(request, id):
	if request.user.is_authenticated:
		customer = request.user.customer
		if customer.watch_list:
			watchlist = customer.watch_list.first()
			print(dir(watchlist))
			# watchproducts = watchlist.products.all()
			# for product in watchproducts:
			# 	if product.product.id == id:
			# 		return dict(color="text-danger", action="remove", is_added=True)
		return dict(color="", action="add", is_added=False)
	else:
		watchlist = cookiewatchlist(request)
		print(watchlist)
		# for product in watchlist:
		# 	if product == id:
		# 		return dict(color="text-danger", action="remove",is_added=True)
		# return dict(color="", action="add",is_added=False)
