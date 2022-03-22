from django.urls import path
from django.contrib.auth.decorators import login_required
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


    path("nuevo", login_required(MascotaCreate.as_view()), name="mascota_crear"),
    path("listar", login_required(MascotaList.as_view()), name="mascota_listar"),

    path("editar/<int:pk>",login_required(MascotaUpdate.as_view()), name="mascota_editar"),
    path("eliminar/<int:pk>", login_required(MascotaDelete.as_view()), name="mascota_eliminar"),

   


 
]
