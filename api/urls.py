from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt import views as jwt_views



app_name= 'api'
router = routers.DefaultRouter()
router.register(r'Products', ListProductsView)
router.register(r'Categories', CategoriesView)
router.register(r'Product-photos', ProductImageView)
router.register(r'Reviews', ReviewsView)
router.register(r'Shop', ShopView)
router.register(r'Specifications', ProductSpecificationView)

urlpatterns = [
	path('', include(router.urls)),
	path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
# urlpatterns+= router.urls