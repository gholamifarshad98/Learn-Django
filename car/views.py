from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework import status, permissions
from .models import Person, Car
from .serializers import CarSerializers, PersonSerializers, CarReadSelrilizers


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializers
    http_method_names = ['get','post','delete','put']
    def list(self, request, *args, **kwargs):
        objs = super().list(self, request, *args, **kwargs)
        print ("=== list ===")
        return objs
    
    def create(self, request, *args, **kwargs):
        obj = super().create(request, *args, **kwargs)
        print("=== create ===")
        return obj
    
    def update(self, request, *args, **kwargs):
        obj = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print("=== update ===> {}".format(instance.name))
        return obj
        
    def retrieve(self, request, *args, **kwargs):
        obj = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print("=== retrieve ===> {}".format(instance.name))
        return obj
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("=== destroy ===> {}".format(instance.name))
        obj = super().destroy(request, *args, **kwargs)
        return obj


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    http_method_names = ["post", "get", "delete", "put"]
    
    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return CarSerializers
        else:
            return CarReadSelrilizers



