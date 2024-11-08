"""
Django settings for Hustle_24 project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import datetime
import re
from django.contrib.messages import constants as messages



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-nam74v@zgf8=0=zgt!q7=7d&=#%jvugqpbidqv6kl#8foorape'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# ALLOWED_HOSTS = ['a9ad-102-89-22-6.eu.ngrok.io']
ALLOWED_HOSTS = [ '.ngrok.io', '127.0.0.1', '.telebit.io' , '.railway.app' , '.loclx.io' , '*' ]
CSRF_TRUSTED_ORIGINS = [
    'https://hustle-24-production.up.railway.app',
    'https://www.hustle-24-production.up.railway.app',
]
# ALLOWED_HOSTS = ['a9ad-102-89-22-6.eu.ngrok.io']

# Application definition

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sessions',
    
    # 'user_sessions',
    'rest_framework',
    'rest_framework.authtoken',
    'crispy_forms',
    'django_extensions',
    'geoip2',
    # 'rest_hooks',

    'carts',
    'accounts.apps.AccountsConfig',
    'watched_products',
    'orders',
    'shop'
]


# HOOK_EVENTS = { }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'user_sessions.middleware.SessionMiddleware',


    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Hustle_24.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'shop.context_processors.categories'
            ],
        },
    },
]

WSGI_APPLICATION = 'Hustle_24.wsgi.application'

# Rest_Framework
REST_FRAMEWORK = {
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.IsAdminUser',
        # 'rest_framework.permissions.NotCreateAndIsAdminUser',
    ],
    # 'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAuthenticated', )
    # 'DEFAULT_RENDERER_CLASSES': [
    #     'rest_framework.renderers.JSONRenderer',
    #     'rest_framework.renderers.AdminRenderer',
    #     'rest_framework.renderers.BrowsableAPIRenderer',
    # ],
}



# JWT settings
# JWT_AUTH = {
#     'JWT_ENCODE_HANDLER':
#     'rest_framework_jwt.utils.jwt_encode_handler',

#     'JWT_DECODE_HANDLER':
#     'rest_framework_jwt.utils.jwt_decode_handler',

#     'JWT_PAYLOAD_HANDLER':
#     'rest_framework_jwt.utils.jwt_payload_handler',

#     'JWT_PAYLOAD_GET_USER_ID_HANDLER':
#     'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

#     'JWT_RESPONSE_PAYLOAD_HANDLER':
#     'rest_framework_jwt.utils.jwt_response_payload_handler',

#     'JWT_SECRET_KEY': SECRET_KEY,
#     'JWT_GET_USER_SECRET_KEY': None,
#     'JWT_PUBLIC_KEY': None,
#     'JWT_PRIVATE_KEY': None,
#     'JWT_ALGORITHM': 'HS256',
#     'JWT_VERIFY': True,
#     'JWT_VERIFY_EXPIRATION': True,
#     'JWT_LEEWAY': 0,
#     'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300),
#     'JWT_AUDIENCE': None,
#     'JWT_ISSUER': None,

#     'JWT_ALLOW_REFRESH': False,
#     'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

#     'JWT_AUTH_HEADER_PREFIX': 'Bearer',
#     'JWT_AUTH_COOKIE': None,
# }


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}



SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = 'images/'
MEDIA_ROOT = Path.joinpath(BASE_DIR, 'static/images')
# STATIC_ROOT = Path.joinpath(BASE_DIR, 'static')
STATICFILES_DIRS =  [
    BASE_DIR / "static",
    BASE_DIR / "static"/ 'images',
    # Path.joinpath(BASE_DIR, '/static/')
]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
]
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = ['accounts.backend.EmailBackend']
LOGIN_REDIRECT_URL = 'accounts:login'
LOGIN_URL = "accounts:login"
LOGOUT_REDIRECT_URL = "shop:home"
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Email


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'ayobamideleewetuga@zohomail.com'
EMAIL_HOST_PASSWORD = 'nRFgFHeDU7Rt'

# Session
CART_SESSION_ID = 'cart'
# SESSION_ENGINE = 'user_sessions.backends.db'
# SILENCED_SYSTEM_CHECKS = ['admin.E410']
GEOIP_PATH = Path.joinpath(BASE_DIR, 'geoip')

# Messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}
