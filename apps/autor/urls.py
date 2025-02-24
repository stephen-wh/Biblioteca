from django.conf.urls import url
from apps.autor.views import autor_delete, AutorDelete, AutorCreate, autor_create, AutorUpdate, autor_edit, autor_list, AutorList
urlpatterns = [
    url(r'^f_listar/$', autor_list, name="f_autor_listar"),
    url(r'^listar/$', AutorList.as_view(), name="autor_listar"),
    url(r'^f_nuevo/$', autor_create, name="f_autor_crear"),
    url(r'^nuevo/$', AutorCreate.as_view(), name="autor_crear"),
    url(r'^f_editar/(?P<pk>\d+)/$', autor_edit, name='f_autor_editar'),
    url(r'^editar/(?P<pk>\d+)/$', AutorUpdate.as_view(), name='autor_editar'),
    url(r'^f_eliminar/(?P<pk>\d+)/$', autor_delete, name='f_autor_eliminar'),
    url(r'^eliminar/(?P<pk>\d+)/$', AutorDelete.as_view(), name='autor_eliminar'),
]