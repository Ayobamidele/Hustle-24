from django.urls import path
from . import  views

urlpatterns = [
    path('cart', views.cart,name="cart"),
    path('cart/update-item', views.update_item, name="update-item"),
    path('cart/process-order', views.process_order, name="process-order"),
    path('cart/checkout', views.checkout,name="checkout"),
    # path('cart/login/checkout', views.checkout,name="c

]