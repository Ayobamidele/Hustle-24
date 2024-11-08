from rest_framework import generics,viewsets,status,views
from shop.models import Product
from accounts.models import User
from .serializers.account_serializers import *
from .serializers.shop_serializers import *
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from django.http import JsonResponse
from django.core.files.uploadedfile import UploadedFile
import requests
import urllib
from PIL import Image
from rest_framework.permissions import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated


User = get_user_model()

class RegistrationView(views.APIView):
    # queryset = User.objects.all()
    # serializer_class = RegistrationSerializer
    permission_classes = (IsNotAuthenticated | AdminAuthenticationPermission,)
    # permission_classes = (IsAuthenticated,)


    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

    # def post(self, request, *args, **kwargs):
    #     created_by = request.user
    #     serializer = self.serializer_class(data=request.data, context={"request": request})
    #     print(serializer , serializer.is_valid())
    #     # if serializer.is_valid():
    #     #     serializer.save()
    #     #     return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ListProductsView(viewsets.ModelViewSet):
    """
    Provides a get method handler.
    """
    # http_method_names = ['get',]
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    # permission_classes = (IsAuthenticated,)
    permission_classes = [ NotCreateAndIsAdminUser | IsOwnerOfShop]
    # print(dir(permission_classes))
    # renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,)

    def create(self, request, *args, **kwargs):
        created_by = request.user
        serializer = self.serializer_class(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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



class ReviewsView(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all()
    serializer_class = ProductReviewSerializer


class ProductSpecificationView(viewsets.ModelViewSet):
    queryset = ProductSpecification.objects.all()
    serializer_class = ProductSpecificationSerializer



class ShopView(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer



class ProductImageView(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer

    def create(self, request, *args, **kwargs):
        created_by = request.user
        if type(request.data.get('image')) == UploadedFile: 
            pass
        elif type(request.data.get('image')) == str:
            post= request.data.copy()
            # url =  + post.get('image')
            # Remove url from the submitted data
            # post['image'] = url
            # Download data from url (requires `requests` module.  Can also be done with urllib)
            post['image'] = UploadedFile(file=open(post['image'], 'rb'))
            # print(UploadedFile(post['image']),0000)
            # request.data.update(post)
            # Set icon field (ImageField) to binary file
            # validated_data['icon'] = UploadedFile(BytesIO(response), name='icon')
            dataT = {'image': post['image'],'alt_text': post['alt_text'], 'is_feature': post['is_feature'], 'product': post['product']}
        serializer = self.serializer_class(data=dataT, context={"request": post})
        print(request.data)
        print(serializer.is_valid(), type(request.data.get('image')), request.data.get('image'))
        print(serializer.errors,222)
        serializer.save(image=post['image'])
        print(serializer.data)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        # if serializer.is_valid():
        # return Response(data={}, status=status.HTTP_400_BAD_REQUEST)

