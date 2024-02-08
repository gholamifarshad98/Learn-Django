from rest_framework import serializers
from .models import Person, Car
 
class PersonSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Person
        fields = "__all__"
        
        
        
        
class CarSerializers(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        
        
class CarReadSelrilizers(serializers.ModelSerializer):
    person = PersonSerializers()
    class Meta:
        model = Car
        fields = "__all__"
        # depth = 1