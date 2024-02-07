from rest_framework.decorators import api_view 
from rest_framework.response import Response
from rest_framework import status

from .models import Employee
from .serializers import EmployeeSerializers

@api_view(["POST"])
def post_Empolyee(request):
    data = {
        'name': request.data['name'],
        'age': request.data['age'],
        'salary': request.data['salary'],
        'post': request.data['post']
    }
    
    ser = EmployeeSerializers(data=data)
    if ser.is_valid():
        ser.save()
        return(Response(ser.data, status= status.HTTP_201_CREATED))    
    else:
        return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)
    
    
@api_view(["GET"])
def get_Employee(request):
    employees = Employee.objects.all() 
    ser = EmployeeSerializers(employees, many = True)
    return Response(ser.data,status= status.HTTP_200_OK)

@api_view(["POST","GET","DELETE"])
def get_update_delete_Empolyee(request,pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except:
        return(Response({"Key":"Not found11"},status= status.HTTP_404_NOT_FOUND ))
    
    if request.method == "GET":
        ser = EmployeeSerializers(employee)
        return Response(ser.data, status= status.HTTP_200_OK)
    elif request.method == "PUT":
        ser = EmployeeSerializers(employee, data= request.data)
        if ser.is_valid():
            ser.save()  
            return(Response(ser.data, status=status.HTTP_200_OK))
        else: 
            return(Response(ser.errors, status=status.HTTP_400_BAD_REQUEST))
        
    elif request.method == "DELETE":
        employee.delete()
        return(Response(status=status.HTTP_204_NO_CONTENT))
        
        
    
    