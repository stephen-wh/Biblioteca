from django import forms
from apps.editor.models import Editor

class EditorForm(forms.ModelForm):
    class Meta:
        model = Editor
        fields = [
            "nombre",
            "domicilio",
            "ciudad",
            "estado", 
            "pais",
            "website",
        ]
        labels = {
            "nombre":"Nombre",
            "domicilio":"Domicilio",
            "ciudad":"Ciudad",
            "estado":"Estado", 
            "pais":"Pais",
            "website":"Sitio web",
        }
        widgets = {
            "nombre":forms.TextInput(attrs={"class":"form-control"}),
            "domicilio":forms.Textarea(attrs={"class":"form-control"}),
            "ciudad":forms.TextInput(attrs={"class":"form-control"}),
            "estado":forms.TextInput(attrs={"class":"form-control"}),
            "pais":forms.TextInput(attrs={"class":"form-control"}),
            "website":forms.TextInput(attrs={"class":"form-control"}),
        }