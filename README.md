# mascotas_django_2022

proyecto de mascotas del tutorial de codigo facilito de django [enlace ](https://www.youtube.com/watch?v=xJseXY2sup8&list=PLsRdPvQ2xMkH8c2BOnQ_O1KZ9lyyL_eGB&index=1)

cambios de version

estoy usando  {% load static %} en vez de {% load staticfiles%} creo que esta esta deprecada


corrigiendo como se hacen los nombres de espacio ahora se hace asi, no se porque

  path('mascota/', include( ('apps.mascota.urls','mascota'), namespace='mascota')),


video 11

poner esto para que lea la carpeta de archivos estaticos en el archivo de configuracion
STATIC_URL = "static/"
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


crear carpeta en la raiz del proyecto y cargar alli los archivos estaticos

14.- Vistas basadas en funciones actualizar y eliminar.

esta es la nueva manera de pasar datos por la url  path("editar/<int:id_mascota>", mascota_edit, name="mascota_editar"), el parametro debe coincidir con el parametro que se masan en la view  def mascota_edit(request, id_mascota):


15.- Vistas basadas en clases, ListView y CreateView

este import cambia 

from django.core.urlresolvers import reverse_lazy a este from django.urls import reverse_lazy


16.- UpdateView y DeleteView, vistas basadas en clases

cuando las vistas se pasar por clase los parametros en la url deben pasarse asi sino django se pone a llorar

path("editar/<int:pk>",MascotaUpdate.as_view(), name="mascota_editar"),
    path("eliminar/<int:pk>", MascotaDelete.as_view(), name="mascota_eliminar"),

    pk debe ser una abreviatura de primary key

17.- CRUD con dos formularios Parte 1
al metodo ForeignKey hay que ponerle el parametro on_delete= sino django llora
persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
18.- CRUD con dos formularios Parte 2
19.- Crear Registro de Usuarios (modelo)
20.- Crear login (facilito)

asi se llaman las vistas del login ahora
  path('accounts/login/', LoginView.as_view(template_name='index.html'), name='login'),
    path('reset/password_reset',PasswordResetView.as_view(template_name='registration/password_reset_email.html'), 
        name='password_reset'), 

21.- Recuperar contraseña por correo (facilito)
22.- Decorador login required
23.- Serializar objetos
24.- Paginación
25.- Restframework ModelSerializer



