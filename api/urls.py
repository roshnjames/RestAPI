from home.views import *;
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from home.views import personmodelview

router1=DefaultRouter()
router1.register(r'personmodelview',personmodelview,basename="personmodelview")

urlpatterns=[
    path('',home,name="home"),
    path('peoples/',peoples,name="peoples"),
    path('classpeoples/',class_peoples.as_view(),name="classpeoples"),
    path('',include(router1.urls))
    
]