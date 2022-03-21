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

