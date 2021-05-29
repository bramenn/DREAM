from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, View
from app.models import Medico
from django.http import HttpResponse 
from IngSoftware import settings


from rest_framework import serializers
from rest_framework.generics import ListAPIView

class MedicoView(TemplateView):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):

		return render(request, self.template_name, {})

class LoginFormView(View):
	template_name = 'login.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})

class MedicoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Medico
		fields = '__all__'

