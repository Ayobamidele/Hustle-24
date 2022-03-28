from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# app_name = 'shop'

urlpatterns = [
    path('', views.home, name="home"),
    # path('shop/<shop>', views.shop, name='shop'),
    path('product/<product>', views.productDetail, name='product'),
    path('<shop>/product/add', views.addProduct, name='addProduct'),
    path('<shop>/<product>/<id>/edit/', views.editProduct, name='editProduct'),
    path('update-photo', views.deleteProductImage, name="update-photo"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
