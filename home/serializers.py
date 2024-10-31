from rest_framework import serializers
from .models import *

class team_serializer(serializers.ModelSerializer):
    class Meta:
        model=team
        fields=['team_name']

class people_serializer(serializers.ModelSerializer):
    team=team_serializer()
    class Meta:
        model=people_details
        fields='__all__'
        depth=1

    #for the validation of the input data
    def validate(self, data):
        special_chars="~!@#$%^&*()_+<>:/|{}[];,.?/"
        if any(x in special_chars for x in data['name']):
            raise serializers.ValidationError("Name should not have special characters!")
        if data['age']<18:
            raise serializers.ValidationError("Person should have age greater than 18!")
        return data