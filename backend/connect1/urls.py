from django.urls import path
from .views import *

urlpatterns=[
    path('',user_registration.as_view(),name="user_registration"),
]