from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(
        max_length=10,
        choices=[
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ]
    )
    contact_number = models.CharField(max_length=10)
    address = models.TextField()
    medical_history = models.TextField(blank=True, null=True)
    emergency_number = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
