from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, reverse_lazy
from django.contrib.auth import views as auth_views
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

    path("password_reset", views.password_reset_request, name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password/password_reset_confirm.html", success_url=reverse_lazy(
        'accounts:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password/password_reset_complete.html'), name='password_reset_complete'),      
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)