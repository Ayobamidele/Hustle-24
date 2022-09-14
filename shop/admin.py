from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Product,
    Shop,
    ProductImage,
    ProductSpecification,
    # ProductSpecificationValue,
    # ProductType,
)

admin.site.register(Shop)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(ProductSpecification)
# admin.site.register(ProductSpecificationValue)
# class ProductSpecificationInline(admin.TabularInline):
#     model = ProductSpecification


# @admin.register(ProductType)
# class ProductTypeAdmin(admin.ModelAdmin):
#     inlines = [
#         ProductSpecificationInline,
#     ]


# class CategoryInline(admin.TabularInline):
#     model = Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductSpecificationInline(admin.TabularInline):
    model = ProductSpecification


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        
        ProductSpecificationInline,
        ProductImageInline,
        # CategoryInline,
    ]