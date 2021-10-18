import os
import random
from PIL import Image
from io import BytesIO
from django.db import models
from django.core.files import File
from django.shortcuts import reverse
from django.contrib.auth.models import User
from accounts.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Product(models.Model):
	title = models.CharField(max_length=100)
	category = models.CharField(max_length=20)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	discount_price = models.FloatField(blank=True, null=True)
	image = models.FileField()
	thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
	description = models.TextField(max_length=1000)
	quantity_available = models.IntegerField(default=1)
	is_featured = models.BooleanField(default=False)
	slug = models.SlugField()
	date_added = models.DateTimeField(auto_now_add=True)

	def slug(self):
		return slugify(self.title)

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

class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    ordering = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return '/%s/' % (self.slug)

class ProductReview(models.Model):
    product = models.ForeignKey(Product, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    stars = models.IntegerField()

    date_added = models.DateTimeField(auto_now_add=True)

def photo_path(instance, filename):	
	basefilename, file_extension= os.path.splitext(filename)
	chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
	randomstr = ''.join((random.choice(chars)) for x in range(10))
	return 'images/userphotos/{userid}/{basename}{randomstring}{ext}'.format(userid= instance.user.id, basename= basefilename, randomstring= randomstr, ext= file_extension)
            

class ProductImage(models.Model):
	product = models.ForeignKey(Product, related_name='images', default=None, on_delete=models.CASCADE)
	images = models.FileField()
	thumbnail = models.ImageField(upload_to= photo_path, blank=True, null=True)
	is_main = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		self.thumbnail = self.make_thumbnail(self.image)
		super().save(*args, **kwargs)

	def make_thumbnail(self, image, size=(300, 200)):
		img = Image.open(image)
		img.convert('RGB')
		img.thumbnail(size)
		thumb_io = BytesIO()
		img.save(thumb_io, 'JPEG', quality=85)
		thumbnail = File(thumb_io, name=image.name)
		return thumbnail