from django.contrib import admin

from .models import Shop,Product,ProductImage,ProductReview,Category
# Register your models here.

admin.site.register(Shop)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductReview)