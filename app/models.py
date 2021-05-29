from django.db import models as m

class Medico(m.Model):
    id = m.CharField(max_length=50, primary_key=True)
    nombre = m.CharField(max_length=50)
    passwor = m.CharField(max_length=100, blank=False)



    class Meta:
        ordering  = ["id"]
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"

    def __str__(self):
        return self.nombre

class Mamography(m.Model):
    imagen = m.FileField(upload_to="mamografias", null=True)
    birad = m.CharField(verbose_name="tipo de cancer", max_length=50)

    class Meta:
        ordering = ["birad"]
        verbose_name = "mamografia"
        verbose_name_plural ="mamografias"

    def __str__(self):
        return self.birad
    
