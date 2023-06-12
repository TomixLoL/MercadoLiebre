from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models

# **** Categoría de Productos


class ProductoCategoriaDetail(DetailView):
    model = models.ProductoCategoria


class ProductoCategoriaList(ListView):
    model = models.ProductoCategoria

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.ProductoCategoria.objects.filter(nombre__icontains=query)
        else:
            object_list = models.ProductoCategoria.objects.all()
        return object_list


class ProductoCategoriaCreate(CreateView):
    model = models.ProductoCategoria
    form_class = forms.ProductoCategoriaForm
    success_url = reverse_lazy("producto:index")


class ProductoCategoriaDelete(DeleteView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")


class ProductoCategoriaUpdate(UpdateView):
    model = models.ProductoCategoria
    success_url = reverse_lazy("producto:productocategoria_list")
    form_class = forms.ProductoCategoriaForm


# *** Producto


class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:index")


class ProductoList(ListView):
    model = models.Producto

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Producto.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Producto.objects.all()
        return object_list


class ProductoDetail(DetailView):
    model = models.Producto


class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")


class ProductoUpdate(UpdateView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")
    form_class = forms.ProductoForm
