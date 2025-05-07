from . models import Doctor
from rest_framework import serializers

class doctor_serializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ['created_at','patient']