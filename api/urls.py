from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

app_name= 'api'
router = routers.DefaultRouter()
router.register(r'Products', ListProductsView)
router.register(r'Categories', CategoriesView)
router.register(r'Product-photos', ProductImageView)
router.register(r'Reviews', ReviewsView)
router.register(r'Specifications', ProductSpecificationView)

urlpatterns = [
	path('', include(router.urls)),
	path('api-token-auth/', obtain_auth_token, name='api_token_auth')
]
# urlpatterns+= router.urls