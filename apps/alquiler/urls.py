from django.urls import path
from apps.alquiler.views import AlquilerView, CrearAlquilerView, CrearDuenoView
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns=[
    path("",AlquilerView.as_view(), name="mis_alquileres"),
    path("crearalquiler/",CrearAlquilerView.as_view(), name="crear_alquiler"),
    path("creardueno/",CrearDuenoView.as_view(), name="crear_dueno")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)