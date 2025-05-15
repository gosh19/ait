# backend/articulos/models.py
from django.db import models

class Articulo(models.Model):
    codigo = models.CharField(max_length=50, unique=True, blank=False, null=False)
    descripcion = models.TextField(blank=False, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    # Opcional: Campos de fecha de creación y actualización
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"

    class Meta:
        verbose_name = "Artículo"
        verbose_name_plural = "Artículos"
        ordering = ['codigo'] # Ordena por defecto por código