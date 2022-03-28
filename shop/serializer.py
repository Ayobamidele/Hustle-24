from rest_framework import serializers
from shop.models import *
from collections import OrderedDict


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(many=True, view_name='category-detail',
                                                   queryset=Category.objects.all())
    link = serializers.HyperlinkedIdentityField(
        view_name="product",
        lookup_field="title",
        lookup_url_kwarg="product"
    )

    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
