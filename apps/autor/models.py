from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=40)
    email = models.EmailField( blank=True, verbose_name="e-mail")

    class Meta:
        verbose_name_plural = "Autores"

    def __str__(self):
        return "%s" % (self.nombre)
