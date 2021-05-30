
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from app.models import Medico
from django.http import HttpResponse


from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm

from rest_framework import serializers

from django.contrib.auth.views import LoginView, LogoutView

class SignOutView(LogoutView):
    pass

class SignInView(LoginView):
    template_name = 'login.html'

class SignUpView(CreateView):
    model = Medico
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        template_name =  'prueba.html'

        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/incia-sesion/')

class BienvenidaView(TemplateView):
   template_name = 'index.html'



class MedicoView(TemplateView):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):

		return render(request, self.template_name, {})

class LoginFormView(TemplateView):
	template_name = 'login.html'

	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {})

class MedicoSerializer(serializers.ModelSerializer):

	class Meta:
		model = Medico
		fields = '__all__'

