from django.urls import path
from apps.usuario.views import RegistroView
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("registro/", RegistroView.as_view(),name='registro'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)