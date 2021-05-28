from django.contrib import admin
from app.models import Medico, Mamography
class MedicoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
    ) 

class MamoAdmin(admin.ModelAdmin):
    list_display = (
        'imagen',
        'birad',
    ) 


admin.site.register(Medico, MedicoAdmin)
admin.site.register(Mamography, MamoAdmin)
