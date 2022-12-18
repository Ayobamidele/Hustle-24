from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import User

User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'first_name' , "last_name" , "email", "is_superuser","is_staff" ,"is_active" ,"is_customer" ,"is_vendor", "last_login"]
        read_only_fields = ['id',  "is_superuser","is_staff" ,"is_active" ,"is_customer" ,"is_vendor", "last_login"]
        extra_kwargs = {"password": {"write_only": True}}



        