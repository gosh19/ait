# backend/articulos/serializers.py
from rest_framework import serializers
from .models import Articulo

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id', 'codigo', 'descripcion', 'precio'] # Campos a incluir en la API
        # Opcional: Hacer que algunos campos sean solo de lectura si es necesario
        # read_only_fields = ['id'] # El ID generalmente es asignado por la BD