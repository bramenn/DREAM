from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from app.models import Medico
from django.http import HttpResponse 
from django.contrib.auth.views import LoginView

class MedicoView(TemplateView):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):

		return render(request, self.template_name, {})

class LoginFormView(LoginView):
	template_name = 'login.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})