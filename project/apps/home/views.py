from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from producto.models import ProductoCategoria

from . import forms, models
from producto import models


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html", {"messages": "Cuenta creada con exito 👌"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "home/about.html")


class CategoriaListView(ListView):
    model = ProductoCategoria
    template_name = "categorias.html"


def index(request):
    categorias = ProductoCategoria.objects.all()[:4]

    context = {
        "categorias": categorias,
    }

    return render(request, "home/index.html", context)
