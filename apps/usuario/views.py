from django.shortcuts import render
from django.views.generic import CreateView
from apps.usuario.forms import RegistroForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from apps.usuario.serializers import UserSerializer
from rest_framework.views import APIView
import json

from django.http import HttpResponse

# Create your views here.


class RegistroUsuario(CreateView):
	model = User
	template_name = "usuario/registrar.html"
	form_class = RegistroForm
	success_url = reverse_lazy('mascota:mascota_listar')

class UserAPI(APIView):
	serializer = UserSerializer

	def get(self, request, format=None):
		lista = User.objects.all()
		response = self.serializer(lista, many=True)

		return HttpResponse(json.dumps(response.data), content_type='application/json')
