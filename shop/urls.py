from django.urls import path
from . import  views

urlpatterns = [
    path('', views.home,name="home"),
    path('vendor/shop', views.shop, name='shop'),    
]