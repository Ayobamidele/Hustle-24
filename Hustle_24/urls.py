"""Hustle_24 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
# from rest_framework import routers
from shop import views as shop_views

# from watched_products import views as watched_products_views

# router = routers.DefaultRouter()
# router.register(r'home', shop_views.ProductsViewSet)
# router.register(r'Categories', shop_views.CategoriesViewSet)
# router.register(r'Product-Images', shop_views.ProductImagesViewSet)
# router.register(r'Product-Images', shop_views.ProductImagesViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
    path('', include('shop.urls', namespace='shop')),
    # path('', include(('shop.urls', 'shop'))),
    path('', include('accounts.urls')),
    path('', include('carts.urls')),
    path('', include('watched_products.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += router.urls
