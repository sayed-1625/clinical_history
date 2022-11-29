from django.urls import path
from user.views import RegistrarUsuario

urlpatterns = [
    path('registrar_usuario/',RegistrarUsuario.as_view(),name = 'registrar_usuario'),
]