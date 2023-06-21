from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from producto.models import ProductoCategoria
from django.contrib import messages
from .forms import UpdateUserForm
from . import forms


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada con exito 👌")
            return redirect("home:index")
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


@login_required
def profile(request):
    if request.method == "POST":
        user_form = UpdateUserForm(request.POST, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, "Cuenta actualizada con exito 👌")
            return redirect("home:index")
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, "home/profile.html", {"user_form": user_form})
