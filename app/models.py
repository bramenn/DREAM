from django.db import models as m

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Medico(m.Model):
    usuario = m.OneToOneField(User, on_delete=m.CASCADE)
    passwor = m.CharField(max_length=100, blank=False)



    class Meta:
        ordering  = ["usuario"]
        verbose_name = "Medico"
        verbose_name_plural = "Medicos"

    def __str__(self):
        return self.nombre.usuario.username

@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        Medico.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.medico.save()

class Mamography(m.Model):
    imagen = m.ImageField(upload_to="mamografias", null=True)
    birad = m.CharField(verbose_name="tipo de cancer", max_length=50, blank=True)

    class Meta:
        ordering = ["birad"]
        verbose_name = "mamografia"
        verbose_name_plural ="mamografias"

    def __str__(self):
        return self.birad
    
