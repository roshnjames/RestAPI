from rest_framework import serializers
from .models import *

class blogmodelserializer(serializers.ModelSerializer):
    class Meta:
        model=blogmodel
        fields='__all__'

    