from collections import OrderedDict

from rest_framework import serializers
from shop.models import *


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    # category = serializers.HyperlinkedRelatedField(many=True, view_name='category-detail',
    #                                                queryset=Category.objects.all())
    link = serializers.HyperlinkedIdentityField(
        view_name="shop:product",
        lookup_field="title",
        lookup_url_kwarg="product"
    )

    class Meta:
        model = Product
        fields = ('link', 'id', 'title', 'brand', 'price', 'discount_price', 'image','productimages',
                    'description', 'stock')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
