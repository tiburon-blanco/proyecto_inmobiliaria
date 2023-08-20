from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('propiedad/', include('app.propiedad.urls')),
    path('contrato/', include('app.contrato.urls')),
]
