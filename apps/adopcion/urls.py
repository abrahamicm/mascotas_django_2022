
from django.urls import path
from apps.adopcion.views import index

from apps.adopcion.views import SolicitudCreate, SolicitudList

urlpatterns = [
    path('',index),
    path('solicitud/listar', SolicitudList.as_view() , name='solicitud_listar'),
    path("solicitud/nueva", SolicitudCreate.as_view(), name='solicitud_crear'),

 
]
