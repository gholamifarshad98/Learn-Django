from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Person, Car
from .serializers import CarSerializers, PersonSerializers, CarReadSelrilizers

@api_view(["GET", "POST"])
def person_view(request):
    if request.method == "GET":
        persons = Person.objects.all()
        return Response(PersonSerializers(persons, many= True).data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        ser = PersonSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        
        

@api_view(["GET", "POST"])
def car_view(request):
    if request.method == "GET":
        cars = Car.objects.all()
        return Response(CarSerializers(cars, many= True).data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        ser = CarSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        else:
            return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(["GET"])
def information(request):
    cars = Car.objects.all()
    return(Response(CarReadSelrilizers(cars, many= True).data, status=status.HTTP_200_OK))