from .models import *
from rest_framework import serializers

class UserDetails_serializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=UserDetails
        fields=['name','username','profile','email','password']