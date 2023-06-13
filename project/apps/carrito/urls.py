from django.urls import path
from .views import carrito_add, carrito_detail, carrito_delete

app_name = "carrito"

urlpatterns = [
    path("add/<int:producto_id>/", carrito_add, name="carrito_add"),
    path("", carrito_detail, name="carrito_detail"),
    path("delete/<int:producto_id>/", carrito_delete, name="carrito_delete"),
]
