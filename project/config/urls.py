from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(("home.urls", "home"))),
    path("producto/", include(("producto.urls", "producto"))),
    path("venta/", include(("venta.urls", "venta"))),
]

#! Este código es válido en un entorno de desarrollo (DEBUG=True). Noo utilizarlo en un entorno de producción.
if settings.DEBUG == True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
