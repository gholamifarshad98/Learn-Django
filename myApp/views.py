from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

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

@api_view(['POST'])
def calculator(requset):
    try:
        num1 = requset.data["num1"]
        num2 = requset.data["num2"]
        opr = requset.data["opr"]
    except:
        return Response({"error","send num1 num2 and opr"}, status= status.HTTP_400_BAD_REQUEST)
    else:
        if isinstance(num1,int) and isinstance(num2,int):
            if opr == "add":
                return Response({"result": num1+num2}, status=status.HTTP_200_OK)
            elif opr == "divid":
                return Response({"result": num1/num2}, status=status.HTTP_200_OK)
            elif opr == "pro":
                return Response({"result": num1*num2}, status=status.HTTP_200_OK)
            elif opr == "sub":
                return Response({"result": num1-num2}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "please send valid opr."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error","send integer value."}, status= status.HTTP_400_BAD_REQUEST)
        