from django.contrib import admin

# Register your models here.

from .models import User, Customer, Vendor, WatchGroup, WatchGroupMember

admin.site.register(WatchGroup)
admin.site.register(WatchGroupMember)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Vendor)