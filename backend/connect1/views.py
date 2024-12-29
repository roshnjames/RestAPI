from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializer import *


class user_registration(generics.CreateAPIView):
    model=UserDetails
    serializer_class=UserDetails_serializer
