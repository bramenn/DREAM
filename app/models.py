from django.db import models

class Medico(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=50)
    imagen = models.FileField(upload_to="mamografias", null=True)
