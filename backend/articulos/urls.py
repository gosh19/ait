# backend/articulos/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticuloViewSet

# Creamos un router y registramos nuestro ViewSet con él.
router = DefaultRouter()
router.register(r'articulos', ArticuloViewSet, basename='articulo')
# El 'basename' es útil para nombrar las URLs generadas, especialmente si el queryset en el ViewSet es complejo.

# Las URLs de la API son determinadas automáticamente por el router.
urlpatterns = [
    path('', include(router.urls)),
]