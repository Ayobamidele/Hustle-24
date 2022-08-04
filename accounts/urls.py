from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views

app_name = "accounts"

urlpatterns = [
    path('accounts/signup/customer/', views.registerCustomer, name="customer_signup"),
    path('accounts/signup/vendor/', views.registerVendor, name="vendor_signup"),
    
    path('login/', views.loginPage, name='login'),
    # path('login/', views.LoginView.as_view(), name='login'),

    path('logout/', views.logoutUser, name='logout'),

    path('customer/<customer>', views.customerPage, name='customer'),
    path('vendor/<vendor>', views.vendorPage, name='vendor'),
    path('account/', views.accountSettings, name='account'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)