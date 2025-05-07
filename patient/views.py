# doctor/views.py
from django.shortcuts import render
from .models import Patient
from .serializer import Patient_serializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

class PatientListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = Patient_serializer

class AddPatient(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = Patient_serializer
    
class RetrievePatient(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = Patient_serializer
    lookup_field = 'id'
    
class RemovePatient(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = Patient_serializer
    lookup_field = 'id'

class UpdatePatient(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Patient.objects.all()
    serializer_class = Patient_serializer
    lookup_field = 'id'
