from django.urls import path
from .views import DoctorListApi, AddDoctor, RetrieveDoctor, RemoveDoctor, UpdateDoctor, DoctorPatientMappingView, PatientDoctorListView, RemoveDoctorFromPatientView

urlpatterns = [
    path('', DoctorListApi.as_view()),
    path('add/', AddDoctor.as_view()),
    path('<int:id>/', RetrieveDoctor.as_view()),
    path('<int:id>/update/', UpdateDoctor.as_view()),
    path('<int:id>/delete/', RemoveDoctor.as_view()),
    path('mappings/', DoctorPatientMappingView.as_view()),
    path('mappings/<int:patient_id>/', PatientDoctorListView.as_view()),
    path('mappings/<int:id>/remove/', RemoveDoctorFromPatientView.as_view())
]
