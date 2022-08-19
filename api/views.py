from rest_framework import generics,viewsets,status
from shop.models import Product
from .serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.files.uploadedfile import UploadedFile
import requests
import urllib
from PIL import Image



class ListProductsView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    # http_method_names = ['get',]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    # parser_classes = (MultiPartParser, FormParser)
    # permission_classes = [ReadOnly, NotCreateAndIsAdminUser | IsOwner]
    # renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)

    def create(self, request, *args, **kwargs):
        created_by = request.user
        serializer = self.serializer_class(data=request.data)
        print(serializer.is_valid())
        print(serializer.errors)
        # if serializer.is_valid():
        return Response(data={}, status=status.HTTP_400_BAD_REQUEST)

        #     serializer.save(created_by=created_by)
        #     return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# def create(self, validated_data):
#         print(validated_data,2222)
#         category_data = validated_data.pop('category')
#         # image_data = validated_data.pop('image')
#         product = Product.objects.create(**validated_data)
#         read_only_fields = ['id',]
#         for category in category_data:
#             category_item, created = Category.objects.get_or_create(name=category.get('name'),slug=category.get('slug'))
#             product.category.add(category_item)
#         # for image in image_data:
#         #     image_item, created = ProductImage.objects.get_or_create(product=product,image=image.get('image'),
#         #         alt_text=image.get('alt_text'),is_feature=image.get('is_feature') )
#         #     image_item.add(image_item)
#         return product

class CategoriesView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductImageView(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def create(self, request, *args, **kwargs):
        created_by = request.user
        serializer = self.serializer_class(data=request.data)
        print(serializer.is_valid(), type(request.data.get('image')), type(request.data.get('alt_text')))
        print(serializer.errors,222, dir(request.data.get('image')) )
        if type(request.data.get('image')) == UploadedFile: 
            pass
        elif type(request.data.get('image')) == str:
            request.query_params._mutable = True
            post= request.data.copy()
            url = "file:///" + post.get('image')
            # Remove url from the submitted data
            post['image'] = ''
            # Download data from url (requires `requests` module.  Can also be done with urllib)
            post['image']= Image.open(urllib.request.urlopen(url))
            request.data = post
            print(request.data.get('image'))
            # Set icon field (ImageField) to binary file
            # validated_data['icon'] = UploadedFile(BytesIO(response), name='icon')
        
        # if serializer.is_valid():
        return Response(data={}, status=status.HTTP_400_BAD_REQUEST)

