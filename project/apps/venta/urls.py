from django.contrib.admin.views.decorators import staff_member_required
from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="venta/index.html"), name="index"),
    path("venta/list/", views.VentaList.as_view(), name="venta_list"),
    path("venta/detail/<int:pk>", views.VentaDetail.as_view(), name="venta_detail"),
    path("venta/create/", staff_member_required(views.VentaCreate.as_view()), name="venta_create"),
    path("venta/delete/<int:pk>", staff_member_required(views.VentaDelete.as_view()), name="venta_delete"),
    path("venta/update/<int:pk>", staff_member_required(views.VentaUpdate.as_view()), name="venta_update"),
]
