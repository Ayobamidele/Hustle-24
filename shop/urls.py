from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home,name="home"),
    path('shop/<shop>', views.shop, name='shop'),
    path('shop/<shop>/<product>', views.productDetail, name='product'),    
]