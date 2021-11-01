from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('accounts/signup/customer/', views.registerPageCustomer, name="customer_signup"),
    path('accounts/signup/vendor/', views.registerPageVendor, name="vendor_signup"),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('customer/<str:pk>', views.customerPage, name='customer'),
    path('vendor/<int:pk>', views.vendorPage, name='vendor'),
    path('account/', views.accountSettings, name='account'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)