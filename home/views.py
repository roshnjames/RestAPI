from rest_framework.decorators import api_view
from rest_framework.response import Response

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