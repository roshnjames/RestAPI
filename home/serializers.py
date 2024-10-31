from rest_framework import serializers
from .models import *


class people_serializer(serializers.ModelSerializer):
    class Meta:
        model=people_details
        fields='__all__'