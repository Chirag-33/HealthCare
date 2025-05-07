# doctor/views.py
from django.shortcuts import render
from .models import Doctor
from patient .models import Patient
from .serializer import doctor_serializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class DoctorListApi(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = doctor_serializer

class AddDoctor(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = doctor_serializer
    
class RetrieveDoctor(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = doctor_serializer
    lookup_field = 'id'
    
class RemoveDoctor(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = doctor_serializer
    lookup_field = 'id'

class UpdateDoctor(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Doctor.objects.all()
    serializer_class = doctor_serializer
    lookup_field = 'id'


# Doctor-patient mapping views 
class DoctorPatientMappingView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        doctor_id = request.data.get('doctor_id')
        patient_id = request.data.get('patient_id')

        if not doctor_id and patient_id:
            return Response({'error':'Both the doctor_id and the patient_id is required '})
        
        try:
            doctor = Doctor.objects.get(id = doctor_id)
            patient = Patient.objects.get(id = patient_id)
            doctor.patient.add(patient)
            return Response({'message':'The doctor is succesfully added'}, status = 200)
        except Doctor.DoesNotExist:
            return Response({'Error':"Doctor not found"},status=400)
        except Patient.DoesNotExist:
            return Response({'Error':'Patient not found'},status=400)

    def get(self, request):
        data = []
        for doctor in Doctor.objects.all():
            patients = doctor.patient.all()
            patient_list = [
                {
                    "patient_id": patient.id,
                    "patient_name": f"{patient.first_name} {patient.last_name}"
                }
                for patient in patients
            ]

            data.append({
                "doctor_id": doctor.id,
                "doctor_name": f"{doctor.first_name} {doctor.last_name}",
                "doctor_email": doctor.email,
                "doctor_phoneNumber": doctor.phone_number,
                "doctor_specialization": doctor.specialization,
                "doctor_licenseNumber": doctor.license_number,
                "doctor_years_of_experience": doctor.years_of_experience,
                "doctor_patients": patient_list  
            })
        return Response(data)

class PatientDoctorListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, patient_id):
        try:
            patient = Patient.objects.get(id = patient_id)
            doctors = patient.doctors.all()
            data = [{
                "doctor_id":doctor.id,
                "doctor_name":f"{doctor.first_name} {doctor.last_name}"
            } for doctor in doctors ]
            return Response(data)
        except Patient.DoesNotExist:
            return Response({"error":'Pateint not found please check the id'}, status = 400)

class RemoveDoctorFromPatientView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, id):
        doctor_id = request.data.get('doctor_id')
        if not doctor_id:
            return Response({"error": "doctor_id is required in body"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            patient = Patient.objects.get(id=id)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

        try:
            doctor = Doctor.objects.get(id=doctor_id)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)

        patient.doctors.remove(doctor)

        return Response({"message": "Doctor removed from patient successfully"}, status=status.HTTP_204_NO_CONTENT)