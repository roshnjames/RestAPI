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
    

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def peoples(request):

    if request.method=="GET":
        people_data=people_details.objects.all()
        serialized_data=people_serializer(people_data,many=True)
        return Response(serialized_data.data if serialized_data.data else serialized_data.errors)
    
    elif request.method=="POST":
        new_data=request.data
        serialized_data=people_serializer(data=new_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)
    
    elif request.method=="PUT":
        data=request.data
        obj=people_details.objects.get(id=data['id'])
        updated_data=people_serializer(obj,data=data,partial=False)
        if updated_data.is_valid():
            updated_data.save()
            return Response(updated_data.data)
        return Response(updated_data.errors)
    
    elif request.method=="PATCH":
        data=request.data
        obj=people_details.objects.get(id =data['id'])
        serialized_data=people_serializer(obj,data=data,partial=True)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data)
        return Response(serialized_data.errors)
    
    else:
        data=request.data
        obj=people_details.objects.get(id=data['id'])
        if obj.delete():
            return Response({"status":"deleted"})
        return Response({"status":"failed"})