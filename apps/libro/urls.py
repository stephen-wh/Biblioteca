from django.conf.urls import url
from apps.libro.views import index, libro_delete, LibroDelete, libro_edit, LibroUpdate, libro_create, LibroCreate, libro_list, LibroList
urlpatterns = [
    url(r'^$', index, name="home"),
    url(r'^libro/f_listar/$', libro_list, name="f_libro_listar"),
    url(r'^libro/listar/$', LibroList.as_view(), name="libro_listar"),
    url(r'^libro/f_nuevo/$', libro_create, name="f_libro_crear"),
    url(r'^libro/nuevo/$', LibroCreate.as_view(), name="libro_crear"),
    url(r'^libro/f_editar/(?P<pk>\d+)/$', libro_edit, name='f_libro_editar'),
    url(r'^libro/editar/(?P<pk>\d+)/$', LibroUpdate.as_view(), name='libro_editar'),
    url(r'^libro/f_eliminar/(?P<pk>\d+)/$', libro_delete, name='f_libro_eliminar'),
    url(r'^libro/eliminar/(?P<pk>\d+)/$', LibroDelete.as_view(), name='libro_eliminar'),
]