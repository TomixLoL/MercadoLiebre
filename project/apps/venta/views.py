from typing import Any, Dict

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from . import forms, models


class VentaDetail(DetailView):
    model = models.Venta


class VentaList(ListView):
    model = models.Venta

    def get_queryset(self):
        if self.request.GET.get("consulta"):
            query = self.request.GET.get("consulta")
            object_list = models.Venta.objects.filter(nombre__icontains=query)
        else:
            object_list = models.Venta.objects.all()
        return object_list


class VentaCreate(CreateView):
    model = models.Venta
    form_class = forms.VentaForm
    success_url = reverse_lazy("venta:index")

    def form_valid(self, form):
        form.instance.vendedor = self.request.user.vendedor
        return super().form_valid(form)


class VentaDelete(DeleteView):
    model = models.Venta
    success_url = reverse_lazy("venta:venta_list")


class VentaUpdate(UpdateView):
    model = models.Venta
    success_url = reverse_lazy("venta:venta_list")
    form_class = forms.VentaForm
