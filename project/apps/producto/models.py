from django.db import models
from django.utils import timezone


class ProductoCategoria(models.Model):
    """Categorías de productos."""

    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=250, null=True, blank=True, verbose_name="descripción")

    class Meta:
        verbose_name = "categoría de productos"
        verbose_name_plural = "categorías de productos"

    def __str__(self):
        """Representa una instancia de la clase como una cadena de texto."""
        return self.nombre


class Producto(models.Model):
    """Productos que corresponden a una categoría."""

    categoria = models.ForeignKey(ProductoCategoria, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="categoría")
    nombre = models.CharField(max_length=100)
    unidad_de_medida = models.CharField(max_length=50)
    cantidad = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.CharField(max_length=250, blank=True, null=True, verbose_name="descripción")
    fecha_actualizacion = models.DateTimeField(default=timezone.now, editable=False, verbose_name="fecha de actualización")

    class Meta:
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return f"{self.nombre} ({self.unidad_de_medida}) ${self.precio:.2f}"
