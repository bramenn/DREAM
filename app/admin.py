from django.contrib import admin
from app.models import Medico
class MedicoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'imagen',
    ) 


admin.site.register(Medico, MedicoAdmin)
