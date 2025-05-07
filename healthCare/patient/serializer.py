from . models import Patient
from rest_framework import serializers

class Patient_serializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ['created_at','updated_at',]