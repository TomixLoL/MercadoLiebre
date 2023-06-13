from atexit import register
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from carrito.models import CarritoItem
from producto.models import Producto


@login_required
def carrito_add(request, producto_id):
    producto = get_object_or_404(Producto, pk=producto_id)
    carrito_item, created = CarritoItem.objects.get_or_create(user=request.user, producto=producto)
    if not created:
        carrito_item.cantidad += 1
        carrito_item.save()
    return redirect("carrito:carrito_detail")


@login_required
def carrito_detail(request):
    carrito_items = CarritoItem.objects.filter(user=request.user)
    return render(request, "carrito/carrito_detail.html", {"carrito_items": carrito_items})


@login_required
def carrito_delete(request, producto_id):
    carrito_item = get_object_or_404(CarritoItem, pk=producto_id, user=request.user)
    carrito_item.delete()
    return redirect("carrito:carrito_detail")
