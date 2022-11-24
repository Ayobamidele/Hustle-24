from .models import *
from django.conf import settings
from shop.models import Product



class Cart(object):

    def __init__(self, request):
        """
        Initialize the cart.
        """
        if request.user.is_authenticated:
        	self.user = request.user
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['regular_price'] = item['product'].regular_price
            item['total_price'] = item['regular_price'] * item['quantity']
            yield item

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        print(type(product.id))
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                      'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()
        print(self.cart,self.cart.keys())


    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True

    def merge(self, id):
    	customers_cart = Cart.objects.get(id=id , active=True)
    	for item in self.cart:
    		print(item)

    def get_total_price(self):
        return sum(item['regular_price'] * item['quantity'] for item in self.cart.values())