from django.urls import path
from apps.alquiler.views import AlquilerView, CrearAlquilerView, CrearDuenoView, EditarAlquilerView, EliminarAlquilerView, ImprimirAlquilerView
from django.conf.urls.static import static
from django.conf import settings
from . import views
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.decorators import method_decorator
urlpatterns=[
    path("",AlquilerView.as_view(), name="mis_alquileres"),
    path("crearalquiler/",CrearAlquilerView.as_view(), name="crear_alquiler"),
    path("creardueno/",CrearDuenoView.as_view(), name="crear_dueno"),
    path("editaralquiler/<int:pk>",EditarAlquilerView.as_view(), name="editar_alquiler"),
    path("eliminaralquiler/<int:pk>",EliminarAlquilerView.as_view(), name="eliminar_alquiler"),
    path("imprimir_alquileres/",method_decorator(xframe_options_exempt, name='dispatch')(ImprimirAlquilerView.as_view()), name="imprimir_alquileres"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)