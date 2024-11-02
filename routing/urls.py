from django.urls import path
from generic import views

urlpatterns=[
    path('',views.blogmodelviewgp.as_view(),name="bloggp"),
    path('blogppd/<int:pk>/',views.blogmodelviewppd.as_view(),name="blogppd")
]