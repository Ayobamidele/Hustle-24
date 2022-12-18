from django.urls import path

from . import views

app_name ='carts'

urlpatterns = [
    path('cart', views.cart,name="cart"),

    path('cart/add', views.addItem,name="add"),
    path('cart/remove', views.removeItem,name="remove"),
    path('cart/status', views.status, name="status"),
    path('cart/remove-all', views.removeAllItems, name="removeAll"),

    # path('cart/messages', views.send_messages, name="messages"),
    path('cart/checkout/auth', views.checkout_authentication,name="checkout_auth"),
    path('cart/checkout/location', views.checkout_location,name="checkout_location"),

    path('cart/process-order', views.processOrder,name="process-order"),
    # path('cart/login/checkout', views.checkout,name="c

]