from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

app_name= 'api'
router = routers.DefaultRouter()
router.register(r'products', ListProductsView)
router.register(r'categories', CategoriesView)
router.register(r'product-photo', ProductImageView)

urlpatterns = [
	path('', include(router.urls)),
	path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
# urlpatterns+= router.urls