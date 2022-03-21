# mascotas_django_2022

proyecto de mascotas del tutorial de codigo facilito de django [enlace ](https://www.youtube.com/watch?v=xJseXY2sup8&list=PLsRdPvQ2xMkH8c2BOnQ_O1KZ9lyyL_eGB&index=1)

cambios de version

estoy usando  {% load static %} en vez de {% load staticfiles%} creo que esta esta deprecada


corrigiendo como se hacen los nombres de espacio ahora se hace asi, no se porque

  path('mascota/', include( ('apps.mascota.urls','mascota'), namespace='mascota')),
  
