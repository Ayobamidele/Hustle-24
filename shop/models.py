import os
import random
from PIL import Image
from io import BytesIO
from django.db import models
from django.core.files import File
from django.urls import reverse
from django.template.defaultfilters import slugify
from watched_products.models import WatchList


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop.product_list_by_category', args=[self.slug])


def photo_path(instance, filename):
    base_file_name, file_extension = os.path.splitext(filename)
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    random_str = ''.join((random.choice(chars)) for _ in range(10))
    return 'images/{basename}{randomstring}{ext}'.format(userid=instance.user.id, basename=base_file_name,
                                                         randomstring=random_str, ext=file_extension)


def make_thumbnail(image, size=(300, 200)):
    img = Image.open(image)
    img.convert('RGB')
    img.thumbnail(size)
    thumb_io = BytesIO()
    img.save(thumb_io, 'JPEG', quality=85)
    thumbnail = File(thumb_io, name=image.name)
    return thumbnail


class ProductImage(models.Model):
    images = models.FileField()
    is_main = models.BooleanField(default=False)
    thumbnail = models.ImageField()

    def __str__(self):
        return str(self.images)

    def save(self, **kwargs):
        make_thumbnail(self.images)


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ManyToManyField(Category, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    brand = models.CharField(max_length=1000, null=True)
    discount_price = models.FloatField(blank=True, null=True)
    image = models.FileField()
    productimages = models.ManyToManyField(ProductImage, )
    thumbnail = models.ImageField(upload_to=photo_path, default='victor-aldabalde-HguvvRqNgxo-unsplash.jpg')
    description = models.TextField(max_length=1000)
    stock = models.IntegerField(default=0)
    available = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    slug = models.SlugField(default=' ')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def save(self, **kwargs):
        self.slug = slugify(self.title)
        return self.slug

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product", kwargs={
            'slug': self.slug
        })

    def get_add_to_cart_url(self):
        return reverse("shop:add-to-cart", kwargs={
            'slug': self.slug
        })

    def get_remove_from_cart_url(self):
        return reverse("shop:remove-from-cart", kwargs={
            'slug': self.slug
        })


class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    customer = models.ForeignKey(to='accounts.Customer', related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)


class Shop(models.Model):
    vendor = models.OneToOneField(to='accounts.Vendor', on_delete=models.CASCADE, null=True, related_name='+')
    shopname = models.CharField(max_length=200, null=True)
    products = models.ManyToManyField(Product, )
    review = models.ManyToManyField(ProductReview, blank=True)

    def __str__(self):
        return self.shopname


class WatchedProduct(models.Model):
    watch_list = models.ForeignKey(WatchList, on_delete=models.CASCADE, null=False, related_name="WatchList")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    initial_Price = models.DecimalField(decimal_places=2, max_digits=100)
    initial_quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{self.product} - {self.watch_list}"
