from rest_framework import serializers
from shop.models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        queryset = Product.objects.all()
        fields = ['url', 'title', 'price', 'brand', 'discount_price', 'image', 'thumbnail', 'description', 'stock',
                  'available', 'is_featured', 'date_added']
