from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import UsuariosViewSet



# Crear el router y registrar el viewset
router = DefaultRouter()

router.register('api/usuarios', UsuariosViewSet, basename= 'Usuarios')

urlpatterns = [
    path('',include(router.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
