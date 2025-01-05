from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',user_registration.as_view(),name="user_registration"),
    path('reg_users/',reg_users.as_view(),name="reg_users")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)