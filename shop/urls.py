from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import  views
from rest_framework.urlpatterns import format_suffix_patterns


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   

    # path('homepage', views.HomePage.as_view()),
    path('', views.home,name="home"),
    # path('shop/<shop>', views.shop, name='shop'),
    path('product/<product>', views.productDetail, name='product'),    
    path('<shop>/product/add', views.addProduct, name='addProduct'),
    path('<shop>/<product>/<id>/edit/', views.editProduct, name='editProduct'), 
    path('updatephoto', views.deleteProductImage,name="updatephoto"),

]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)