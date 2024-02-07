from rest_framework import serializers
from .models import Employee
from django.utils import timezone

class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ("created_at","updated_at")
    
    def validate_name(self, value):
        if value == "Ahmad":
            raise serializers.ValidationError("You are blocked.")
        else:
            return(value)
    def create(self, Validate_data):
        obj = super().create(Validate_data)
        obj.created_at = timezone.now()
        obj.save()
        return obj
    def update(self, instance, validated_data):
        old_created_at = instance.created_at
        obj = super().update(instance, validated_data)
        obj.created_at = old_created_at
        obj.updated_at = timezone.now()
        obj.save()
        return(obj)