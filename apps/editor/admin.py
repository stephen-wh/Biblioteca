from django.contrib import admin
from apps.editor.models import Editor 


# Registrar el modelo Editor en el admin
class EditorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'domicilio', 'ciudad', 'pais')  # Muestra estos campos en el listado
    search_fields = ('nombre', 'pais')  # Permite buscar por nombre y país
    list_filter = ('pais',)  # Filtro para el campo 'pais'

admin.site.register(Editor, EditorAdmin)
