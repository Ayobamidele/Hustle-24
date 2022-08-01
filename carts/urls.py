from django.urls import path

from . import views

app_name ='carts'

urlpatterns = [
    path('cart', views.cart,name="cart"),
    path('cart/update-item', views.updateItem,name="update-item"),
    path('cart/process-order', views.processOrder,name="process-order"),
    path('cart/checkout', views.checkout,name="checkout"),
    # path('cart/login/checkout', views.checkout,name="c

]