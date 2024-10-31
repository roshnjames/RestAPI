from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

@api_view(['GET','POST'])
def home(request):
    if request.method=="GET":
        get_resp={
            'name':'roshin',
            'lname':'james',
            'age':'24'
        }
        return Response(get_resp)
    elif request.method=="POST":
        post_resp={
            'method':'post'
        }
        return Response(post_resp)
    

@api_view(['GET','POST'])
def peoples(request):
    if request.method=="GET":
        people_data=people_details.objects.all()
        serialized_data=people_serializer(people_data,many=True)
        return Response(serialized_data.data if serialized_data.data else serialized_data.errors) 
    