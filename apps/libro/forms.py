from django import forms
from apps.libro.models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = [
            "titulo",
            "autores", 
            "editor", 
            "fecha_publicacion",
            "portada",
        ]
        labels = {
            "titulo": "Titulo",
            "autores": "Autores", 
            "editor": "Editor", 
            "fecha_publicacion": "Fecha de publicacion",
            "portada": "Portada",
        }
        widgets = {
            "titulo": forms.TextInput(attrs={"class":"form-control"}),
            "autores": forms.CheckboxSelectMultiple(attrs={}),
            "editor": forms.Select(attrs={"class":"form-control"}),
            "fecha_publicacion": forms.TextInput(attrs={"class": "form-control", "type": "date",},), 
        }