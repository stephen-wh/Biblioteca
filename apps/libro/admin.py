from django.contrib import admin
from apps.libro.models import Libro

class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo','editor', 'fecha_publicacion',)  # Muestra estos campos en el listado
    list_filter = ('fecha_publicacion',)  # Filtro para el campo 'fecha_publicacion'
    date_hierarchy = "fecha_publicacion"
    ordering = ("-fecha_publicacion",)
    filter_horizontal = ('autores',)  # Filtro para el campo 'autores' (ManyToManyField)
    raw_id_fields = ("editor",)
    #search_fields = ('titulo',)  # Permite buscar por título
    
    

admin.site.register(Libro, LibroAdmin)
