from django.contrib import admin
from apps.autor.models import Autor


# Registrar el modelo Autor en el admin
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'email')  # Muestra estos campos en el listado
    search_fields = ('nombre', 'apellidos')  # Permite buscar por nombre y apellidos
    list_filter = ('email',)  # Filtro para el campo 'email'
    
admin.site.register(Autor, AutorAdmin)