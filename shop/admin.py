from django.contrib import admin

from .models import (Category, Product, ProductImage, ProductReview, Shop,
                     WatchedProduct)

# Register your models here.

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(WatchedProduct)
