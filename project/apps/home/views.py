from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from venta import models

from . import forms


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "home/index.html")


@staff_member_required
def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "home/index.html", {"messages": "Vendedor creado 👌"})
    else:
        form = forms.CustomUserCreationForm()
    return render(request, "home/register.html", {"form": form})


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "home/about.html")
