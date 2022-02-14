from django.contrib import admin

from .models import Cart,Order,OrderItem,ShippingAddressCustomer,ShippingAddressOrder,ShippingPaymentCustomer,ShippingPaymentOrder,CartItem
# Register your models here.

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddressOrder)
admin.site.register(ShippingAddressCustomer)
admin.site.register(ShippingPaymentCustomer)
admin.site.register(ShippingPaymentOrder)
