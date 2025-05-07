
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/patients/', include("patient.urls")),
    path('api/doctor/', include("doctor.urls")),
    path('api/auth/', include("authapi.urls"))
]
