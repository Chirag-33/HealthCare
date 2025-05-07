from django.urls import path
from .views import PatientListApi, AddPatient, UpdatePatient, RemovePatient, RetrievePatient

urlpatterns = [
    path('', PatientListApi.as_view()),
    path('add/', AddPatient.as_view()),
    path('<int:id>/', RetrievePatient.as_view()),
    path('<int:id>/update/', UpdatePatient.as_view()),
    path('<int:id>/delete/', RemovePatient.as_view())
]
