from django.contrib import admin

from .models import Cart,Order,OrderItem,ShippingAddressCustomer,ShippingAddressOrder
# Register your models here.

admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddressOrder)
admin.site.register(ShippingAddressCustomer)