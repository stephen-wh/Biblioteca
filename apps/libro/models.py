from django.db import models
from apps.autor.models import Autor
from apps.editor.models import Editor

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autores = models.ManyToManyField(Autor)
    editor = models.ForeignKey(Editor)
    fecha_publicacion = models.DateField(blank=True, null=True)
    portada = models.ImageField(upload_to="portadas/", blank=True, null=True)

    def __str__(self):
        return "%s" % (self.titulo)
