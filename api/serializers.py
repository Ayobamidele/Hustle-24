from os import ctermid
from typing_extensions import Required
from unicodedata import category
from rest_framework import serializers
from shop.models import *
from rest_flex_fields import FlexFieldsModelSerializer
from versatileimagefield.serializers import VersatileImageFieldSerializer
from drf_extra_fields.fields import Base64ImageField
import urllib
from django.core.files.base import ContentFile
from PIL import Image
from django.core.files.uploadedfile import UploadedFile
import requests


class ProductImageSerializer(serializers.ModelSerializer):
    # product = serializers.ReadOnlyField(required=False)
    image =  serializers.SerializerMethodField()
    
    class Meta:
        model = ProductImage
        # fields = '__all__'
        fields = ['alt_text', 'image', 'is_feature']
        read_only_fields = ['id']
        extra_kwargs = {
            'image': {'validators': []},
            'product': {'validators': []},
        }

    # def validate_image(self, value):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     # if 'django' not in value.lower():
    #         # raise serializers.ValidationError("Blog post is not about Django")
    #     print(data,"Right here Q")
    #     return value

    # def validate(self, data):
    #     CONTEXT_OBJ = self.context.get('request')
    #     print(data,"Right here Q")

    # def create(self, validated_data):
    #     print(validated_data,123456)
    #     data = self.context['request']
    #     print(data.keys(), data.get('image'))
    #     data_product = Product.objects.get(id=data.get('product'))
    #     photo = ProductImage.objects.create(product=data_product, image=data.get('image'),alt_text=data.get('alt_text'), is_feature=data.get('is_feature'))
    #     # photo.save()
    #     print(photo)
    #     return photo

    def get_image(self, obj):
        request = self.context.get('request')
        print(obj)
        try:
            return obj.image.url
        except Exception as e:
            return obj


class ProductReviewSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductReview
        # fields = ('content' ,)
        fields = '__all__'
        read_only_fields = ['id',]


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields = '__all__'
        extra_kwargs = {
            'name': {'validators': []},
            # 'id': {'read_only': False},
            'slug': {'validators': []},
        }
        read_only_fields = ['id',]
        # exclude=("parent", "lft", "rght",
                #  "level", "tree_id", "is_active", "id")
        # fields = ['name',"is_active"]

    def create(self, validated_data):
        print(validated_data,2222)
        category_data = validated_data.pop('category')
        read_only_fields = ['id',]
        for category in category_data:
            answer, created = Category.objects.get_or_create(name=category.get('name'),slug=category.get('slug'))


class ProductsSerializer(serializers.ModelSerializer):
    category=CategorySerializer(many=True)
    image=ProductImageSerializer(many=True)
    # category=serializers.ListField(child=CategorySerializer(many=True, allow_null=True,))
    # category =serializers.PrimaryKeyRelatedField(many=True, allow_empty=False,queryset=Category.objects.all())
    reviews=ProductReviewSerializer(many=True, read_only=True)
    # images=serializers.SerializerMethodField('get_images')
    link=serializers.HyperlinkedIdentityField(
        view_name="shop:product",
        lookup_field="id",
        lookup_url_kwarg="product",
    )

    class Meta:
        model=Product
        read_only_fields = ['id','image']
        # fields = '__all__'
        fields=(	'link', 'title', 'regular_price', 'discount_price',
                	'description', 'stock', 'created_at', 'category', 'image',
                    'reviews'	)


    # def create(self, validate_data):
    #     category_data=validate_data.pop('category')
    #     category_id=Category.objects.create(**validate_data)

    #     for details in category_data:
    #         Category.objects.create(sequence_id=category_id, **details)
    #     return category_id

    # def get_images(self, product):
    #    return ProductImageSerializer(product.product_image.all(), many=True, context=self.context).data


    # def get_catigories(self, product):
    #    return CategorySerializer(product.product_category.all(), many=True, context=self.context).data
