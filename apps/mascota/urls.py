from django.urls import path
from apps.mascota.views import (
    MascotaCreate,
    MascotaList,
    MascotaUpdate,
    MascotaDelete,
    index,
    mascota_view,
    mascota_list,
    mascota_edit,
    mascota_delete,
)

urlpatterns = [
    path("", index, name="index"),


    path("nuevo", MascotaCreate.as_view(), name="mascota_crear"),
    path("listar", MascotaList.as_view(), name="mascota_listar"),

    path("editar/<int:pk>",MascotaUpdate.as_view(), name="mascota_editar"),
    path("eliminar/<int:pk>", MascotaDelete.as_view(), name="mascota_eliminar"),

   


 
]
