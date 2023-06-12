from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="producto/index.html"), name="index"),
    path("productocategoria/detail/<int:pk>", views.ProductoCategoriaDetail.as_view(), name="productocategoria_detail"),
    path("productocategoria/list/", views.ProductoCategoriaList.as_view(), name="productocategoria_list"),
    path("productocategoria/create/", staff_member_required(views.ProductoCategoriaCreate.as_view()), name="productocategoria_create"),
    path("productocategoria/delete/<int:pk>", staff_member_required(views.ProductoCategoriaDelete.as_view()), name="productocategoria_delete"),
    path("productocategoria/update/<int:pk>", staff_member_required(views.ProductoCategoriaUpdate.as_view()), name="productocategoria_update"),
    path("producto/detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    path("producto/list/", views.ProductoList.as_view(), name="producto_list"),
    path("producto/create/", staff_member_required(views.ProductoCreate.as_view()), name="producto_create"),
    path("producto/delete/<int:pk>", staff_member_required(views.ProductoDelete.as_view()), name="producto_delete"),
    path("producto/update/<int:pk>", staff_member_required(views.ProductoUpdate.as_view()), name="producto_update"),
]
