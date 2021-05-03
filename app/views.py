from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from app.models import Medico
from django.http import HttpResponse 

class MedicoView(TemplateView):
	template_name = 'index.html'

	def get(self, request, *args, **kwargs):
		

		if request.GET:
			medico = Medico()
			medico.nombre = "Carlos Hincapie"
			medico.imagen = request.FILES.get('txtImagen')
			print(request.FILES.get('txtImagen'))
			medico.save()

		return render(request, self.template_name, {})