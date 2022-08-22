import os
import random
from io import BytesIO
from itertools import product
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files import File
from django.db import models
from django.template.defaultfilters import slugify
from accounts.models import *
from django.urls import reverse
from PIL import Image
from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# from mptt.models import MPTTModel, TreeForeignKey
from django.core.files.temp import NamedTemporaryFile
import requests


def photo_path(instance, filename):
    basefilename, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    randomstr = ''.join((random.choice(chars)) for x in range(10))
    return 'images/{basename}{randomstring}{ext}'.format(userid=instance.user.id, basename=basefilename,
                                                         randomstring=randomstr, ext=file_extension)

class Category(models.Model):
    """
    """
    name = models.CharField(
        verbose_name=_("Category Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255, unique=True)
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("shop:category", args=[self.slug])

    def __str__(self):
        return self.name

# class ProductType(models.Model):
#     """
#     ProductType Table will provide a list of the different types
#     of products that are for sale.
#     """

#     name = models.CharField(verbose_name=_("Product Name"), help_text=_(
#         "Required"), max_length=255, unique=True)
#     is_active = models.BooleanField(default=True)

#     class Meta:
#         verbose_name = _("Product Type")
#         verbose_name_plural = _("Product Types")

#     def __str__(self):
#         return self.name


class ProductSpecification(models.Model):
    """
    The Product Specification Table contains product
    specifiction or features for the product types.
    """

    # product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_(
        "Name"), help_text=_("Required"), max_length=255)

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The Product table contining all product items.
    """

    # product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    category = models.ManyToManyField(Category, related_name='category', blank=True)
    title = models.CharField(
        verbose_name=_("title"),
        help_text=_("Required"),
        max_length=255,
    )
    stock = models.IntegerField(default=0)
    description = models.TextField(verbose_name=_(
        "description"), help_text=_("Not Required"), blank=True)
    slug = models.SlugField(max_length=255)
    regular_price = models.DecimalField(
        verbose_name=_("Regular price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change product visibility"),
        default=True,
    )
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
    users_wishlist = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
    
    @property
    def get_absolute_url(self):
        return reverse("shop:product", args=[self.id])

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    """
    The Product Specification Value table holds each of the
    products individual specification or bespoke features.
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(
        ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("value"),
        help_text=_("Product specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The Product Image table.
    """

    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="image", related_query_name='image',null=True, blank=True)
    image = models.ImageField(
        verbose_name=_("image"),

        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alternative text"),
        help_text=_("Please add alternative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural =_("Product Images")


    def __str__(self):
        return f"{self.image} - {self.product}"




class ProductReview(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='review', null=True, blank=True)
    customer = models.ForeignKey(
        to='accounts.Customer', related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True)
    stars = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

class Shop(models.Model):
    vendor = models.OneToOneField(
        to='accounts.Vendor', on_delete=models.CASCADE, null=True, related_name='+')
    shopname = models.CharField(max_length=200, null=True)
    products = models.ManyToManyField(Product, )
    review = models.ManyToManyField(ProductReview, blank=True)

    def __str__(self):
        return self.shopname



