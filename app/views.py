
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from app.models import Medico, Mamography
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm, MamographyForm

from rest_framework import serializers

from django.contrib.auth.views import LoginView, LogoutView

class SignOutView(LogoutView):
    pass

class SignInView(LoginView):
    template_name = 'login_2.html'

class SignUpView(CreateView):
    model = Medico
    form_class = SignUpForm

    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''

        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/incia-sesion/')

class BienvenidaView(TemplateView):
   template_name = 'principal_2.html'

@login_required
def UploadToMammoView(request):
    template_name = 'subir_mamo_2.html'
    if request.method == 'POST':
        print(request.POST)
        form = MamographyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            message = "imagen subida"
    else:
        form = MamographyForm()
    return render(request, template_name, {'form':form})



class MedicoView(TemplateView):
	template_name = 'principal_2.html'

	def get(self, request, *args, **kwargs):

		return render(request, self.template_name, {})


@method_decorator(login_required, name='dispatch')
class PerfilView(TemplateView):
    template_name = 'perfil_2.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name, {})

