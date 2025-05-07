from django.db import models
from patient.models import Patient
# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=10)
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=100, unique=True)
    years_of_experience = models.PositiveSmallIntegerField()
    patient = models.ManyToManyField(Patient, related_name='doctors', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name} {self.specialization}"