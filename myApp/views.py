from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def helloWorld(request):
    return Response({"message":"Hello World"})

@api_view(['GET','POST'])
def hello(request):
    if request.method == 'GET':
        return(Response({"message":"Hello World"}))
    if request.method == "POST":
        return(Response({"message": "Hello {}".format(request.data["name"])}))
    
    return