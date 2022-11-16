# from django.urls import path, include
# from rest_framework import routers
from .views import *
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name= 'whatsapp_api'

urlpatterns = [
    path('webhooks_receive_msg/', views.webhook,name="whatsapp_webhook"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# router = routers.SimpleRouter(trailing_slash=False)
# router.register(r'webhooks', views.HookViewSet, 'webhook')
# router.register(r'webhooks_receive_msg', HookViewSet, 'webhook')
# urlpatterns = router.urls

# urlpatterns = [
# 	path('', include(router.urls)),
# 	# path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
#  #    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
# ]