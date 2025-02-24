from django import forms
from apps.autor.models import Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = [
            "nombre",
            "apellidos",
            "email",
        ]
        labels = {
            "nombre":"Nombre",
            "apellidos":"Apellidos",
            "email":"Email",
        }
        widgets = {
            "nombre":forms.TextInput(attrs={"class":"form-control"}),
            "apellidos":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.TextInput(attrs={"class":"form-control"}),
        }