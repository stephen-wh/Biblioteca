from django.conf.urls import url
from apps.editor.views import editor_delete, EditorDelete, editor_edit, EditorUpdate, editor_create, EditorCreate, editor_list, EditorList
urlpatterns = [
    url(r'^f_listar/$', editor_list, name="f_editor_listar"),
    url(r'^listar/$', EditorList.as_view(), name="editor_listar"),
    url(r'^f_nuevo/$', editor_create, name="f_editor_crear"),
    url(r'^nuevo/$', EditorCreate.as_view(), name="editor_crear"),
    url(r'^f_editar/(?P<pk>\d+)/$', editor_edit, name='f_editor_editar'),
    url(r'^editar/(?P<pk>\d+)/$', EditorUpdate.as_view(), name='editor_editar'),
    url(r'^f_eliminar/(?P<pk>\d+)/$', editor_delete, name='f_editor_eliminar'),
    url(r'^eliminar/(?P<pk>\d+)/$', EditorDelete.as_view(), name='editor_eliminar'),
]