from django.contrib import admin

from .models import Customer, User, Vendor, WatchGroup, WatchGroupMember

# Register your models here.


admin.site.register(WatchGroup)
admin.site.register(WatchGroupMember)
admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Vendor)