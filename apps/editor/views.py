from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from apps.editor.forms import EditorForm
from apps.editor.models import Editor

# Create your views here.

# Crear un editor usando una clase basada en vista
class EditorCreate(SuccessMessageMixin, CreateView):
    model = Editor
    form_class = EditorForm
    template_name = "editor/editor_form.html"
    success_url = reverse_lazy("editor:editor_listar")

    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Editor creado exitosamente")
        return super().form_valid(form)

# Vista para crear un nuevo editor
def editor_create(request):
    if request.method == "POST":
        form = EditorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editor creado exitosamente')
            return redirect("editor:editor_listar")
        else:
            messages.info(request, 'Existen campos faltantes o incorrectos')
    else:
        form = EditorForm()
    return render(request, "editor/editor_form.html", {"form": form})

# Vista para listar editores
def editor_list(request):
    editores = Editor.objects.all().order_by("id")[:3]  # Modifica el número de editores según lo necesites
    contexto = {"editores": editores}
    return render(request, "editor/editor_list.html", contexto)

# Vista para editar un editor
def editor_edit(request, pk):
    editor = get_object_or_404(Editor, id=pk)
    if request.method == "GET":
        form = EditorForm(instance=editor)
    else:
        form = EditorForm(request.POST, instance=editor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editor actualizado exitosamente')
            return redirect("editor:editor_listar")
        else:
            messages.info(request, 'Existen campos faltantes o incorrectos')
    return render(request, "editor/editor_form.html", {"form": form})

# Actualizar un editor usando una clase basada en vista
class EditorUpdate(SuccessMessageMixin, UpdateView):
    model = Editor
    form_class = EditorForm
    template_name = "editor/editor_form.html"
    success_url = reverse_lazy("editor:editor_listar")

    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Editor actualizado exitosamente")
        return super().form_valid(form)

# Listar editores usando una clase basada en vista
class EditorList(ListView):
    model = Editor
    template_name = "editor/editor_list.html"
    context_object_name = "editores"

# Eliminar un editor usando una clase basada en vista
class EditorDelete(DeleteView):
    model = Editor
    template_name = "editor/editor_delete.html"
    success_url = reverse_lazy("editor:editor_listar")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Editor eliminado exitosamente")
        return super().delete(request, *args, **kwargs)

# Vista para eliminar un editor
def editor_delete(request, pk):
    editor = get_object_or_404(Editor, id=pk)
    if request.method == "POST":
        editor.delete()
        messages.success(request, 'Editor eliminado exitosamente')
        return redirect("editor:editor_listar")
    return render(request, "editor/editor_delete.html", {"editor": editor})
