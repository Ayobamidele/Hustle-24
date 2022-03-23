from typing import Any

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .decorators import *
from .models import *
from .utils import cookieCart, cartData, guestOrder

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
import datetime
import random
import json
import os
from accounts.models import *
from accounts.forms import *
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your views here.


def generate_ref_code():
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''.join((random.choice(chars)) for _ in range(10))
    return random_str


def cart(request):
    userPicture = request.user
    if request.user.is_authenticated:
        if request.user.is_customer:
            userPicture = request.user.customer
        elif request.user.is_vendor:
            userPicture = request.user.vendor
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    if request.user.is_authenticated:
        total = cartItems
    else:
        total = order.get('get_cart_items')
    context = {'items': items, 'order': order, 'cartItems': cartItems, 'total': total, 'userPicture': userPicture}
    return render(request, 'carts/cart.html', context)


def update_item(request):
    print(request.body, 22222)
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('Product:', productId)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    print("came here", customer, product, order, orderItem)
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
        order.quantity: int | Any = (order.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
        order.quantity: int | Any = (order.quantity - 1)
    orderItem.save()
    order.save()
    if action == 'removeAll':
        order.quantity = (order.quantity - orderItem.quantity)
        orderItem.delete()
        order.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)


def checkout(request):
    userPicture = request.user
    if request.user.is_authenticated:
        if request.user.is_customer:
            userPicture = request.user.customer
        elif request.user.is_vendor:
            userPicture = request.user.vendor
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    if request.user.is_authenticated:
        display_register = False
        form = CreateUserForm()
    else:
        display_register = True
        form = CreateUserForm()
    context = {'items': items, 'order': order,
               'cartItems': cartItems,
               'display_register': display_register,
               'regform': form,
               'userPicture': userPicture
               }
    return render(request, 'carts/checkout.html', context)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    if request.user.is_authenticated:
        customer = request.user.customer
        customer_order, created = Order.objects.get_or_create(complete=False, customer=customer)
        customer_order.complete = True
        customer_order.is_ordered = True
        customer_order.ref_code = generate_ref_code()
        orderIdv = customer_order.ref_code
        customer_order.save()
        order_items = customer_order.orderitem_set.all()
        for orderItem in order_items:
            orderItem.is_ordered = True
            orderItem.save()
    else:
        cookieData = cookieCart(request)
        cartItems = cookieData['cartItems']
        order = cookieData['each_order']
        items = cookieData['items']
        userData = json.loads(request.body)['form']
        print(cookieCart)
        print(cartItems)
        print(order)
        print(items)
        print(userData)
        print(items)
        # Create user
        print(userData)
        username = userData['first_name'] + " " + userData['last_name']
        password = userData['password']
        print(username, password)
        new_user = User.objects.create_user(username=username,
                                            email=userData['email'],
                                            password=password,
                                            first_name=userData['first_name'],
                                            last_name=userData['last_name']
                                            )
        new_user.save()
        messages.success(request, 'Account was created for ' + username)
        print(new_user.id)
        customer = Customer.objects.get(user=new_user.id)
        print("here")
        customer_order = Order.objects.create(
            customer=customer,
            complete=True,
            is_ordered=True,
            quantity=order['get_cart_items'],
            ref_code=generate_ref_code()
        )
        print('here2')
        customer_order.save()
        orderIdv = customer_order.ref_code
        print(customer_order)
        for item in items:
            product_item = Product.objects.get(id=item['product']['id'])
            print('here3')
            print(product_item, customer_order, item['quantity'])
            orderI = OrderItem.objects.create(
                order=customer_order,
                product=product_item,
                quantity=item['quantity'],
                is_ordered=True,
            )
            print('here4')
            orderI.save()
        """
    Pass in each_order
    Get a each_order
    Get all vendors involved
    Arrange the each_order by vendor Id
    """
    order = customer_order
    print(order)
    order_items = order.get_cart_items()
    print(order_items)
    all_vendors = []
    all_vendors_id = set([])
    sortedAllVendors = {}
    print(all_vendors, all_vendors_id, sortedAllVendors)
    for orderItem in order_items:
        vendorId = orderItem.product.shop_set.first().vendor_id
        all_vendors_id.add(vendorId)
        all_vendors.append({vendorId: [orderItem]})
    print("point 1")
    for id in all_vendors_id:
        sortedAllVendors[id] = []
    print("point 2")

    def add_order(order_id):
        for each_order in all_vendors:
            if order_id in each_order.keys():
                for x in each_order[order_id]:
                    sortedAllVendors[order_id].append(x)

    print("point 3")
    for order in all_vendors_id:
        add_order(order)
    print("point 4")
    for cartkey in sortedAllVendors:
        vendor_user = Vendor.objects.get(id=cartkey)
        vendors_cart = Cart.objects.create()
        vendors_cart.vendor = vendor_user
        print(vendors_cart.vendor)
        vendors_cart.order = customer_order
        print("point 5", vendors_cart)
        for orderedProducts in sortedAllVendors[cartkey]:
            vendors_cart.totalprice += orderedProducts.get_total()
            print(vendors_cart.totalprice)
            product_item = Product.objects.get(id=orderedProducts.product.id)
            vendors_cart.products.add(product_item)
            ordered_product = CartItem.objects.create(
                cart=vendors_cart,
                product=product_item,
                quantity=orderedProducts.quantity,
                is_ordered=True,
            )
            ordered_product.save()
            vendors_cart.quantity += orderedProducts.quantity
            print("point 6")
        print("point 7", vendors_cart)
        vendors_cart.save()
        print("point 8")
    return JsonResponse('Payment complete!', safe=False)
