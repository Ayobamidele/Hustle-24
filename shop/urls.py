from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import  views

urlpatterns = [
    path('', views.home,name="home"),
    path('shop/<shop>', views.shop, name='shop'),
    path('product/<product>', views.productDetail, name='product'),    
    path('<shop>/product/add', views.addProduct, name='addProduct'),
    path('<shop>/<product>/edit/<id>', views.editProduct, name='editProduct'),      
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
