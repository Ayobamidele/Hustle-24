from django.contrib import admin
from .models import WatchList, WatchedProduct

# Register your models here.

admin.site.register(WatchList)
admin.site.register(WatchedProduct)