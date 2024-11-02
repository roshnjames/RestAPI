from rest_framework.response import Response
from .serializers import *
from rest_framework import generics

class blogmodelviewgp(generics.ListCreateAPIView):
    queryset=blogmodel.objects.all()
    serializer_class=blogmodelserializer

class blogmodelviewppd(generics.RetrieveUpdateDestroyAPIView):
    queryset=blogmodel.objects.all()
    serializer_class=blogmodelserializer