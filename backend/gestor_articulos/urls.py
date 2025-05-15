# backend/gestor_articulos/urls.py
from django.contrib import admin
from django.urls import path, include # Asegúrate de que 'include' esté importado

urlpatterns = [
    path('admin/', admin.site.urls),
    # Agregamos la siguiente línea para incluir las URLs de nuestra API
    path('api/', include('articulos.urls')), # Todas las URLs de la app 'articulos' estarán bajo '/api/'
]