from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from apps.autor.forms import AutorForm
from apps.autor.models import Autor

# Vista para listar autores
def autor_list(request):
    autores = Autor.objects.all().order_by("id") 
    contexto = {"autores": autores}
    return render(request, "autor/autor_list.html", contexto)

class AutorList(ListView):
    model = Autor
    template_name = "autor/autor_list.html"
    context_object_name = "autores"

# Vista para crear un nuevo autor
def autor_create(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado exitosamente')
            return redirect("autor:f_autor_listar")
        else:
            messages.info(request, 'Existen campos faltantes o incorrectos')
    else:
        form = AutorForm()
    return render(request, "autor/autor_form.html", {"form": form})

class AutorCreate(SuccessMessageMixin, CreateView):
    model = Autor
    form_class = AutorForm
    template_name = "autor/autor_form.html"
    success_url = reverse_lazy("autor:autor_listar")

    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Autor creado exitosamente")
        return super().form_valid(form)


# Actualizar un autor usando una clase basada en vista
class AutorUpdate(SuccessMessageMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = "autor/autor_form.html"
    success_url = reverse_lazy("autor:autor_listar")

    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Autor actualizado exitosamente")
        return super().form_valid(form)

def autor_edit(request, pk):
    autor = get_object_or_404(Autor, id=pk)
    # autor = Autor.objects.get(id=pk)
    if request.method == "GET":
        form = AutorForm(instance=autor)
    else:
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor actualizado exitosamente')
            return redirect("autor:f_autor_listar")
        else:
            messages.info(request, 'Existen campos faltantes o incorrectos')
    return render(request, "autor/autor_form.html", {"form": form})

# Eliminar un autor usando una clase basada en vista
class AutorDelete(DeleteView):
    model = Autor
    template_name = "autor/autor_delete.html"
    success_url = reverse_lazy("autor:autor_listar")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Autor eliminado exitosamente")
        return super().delete(request, *args, **kwargs)

def autor_delete(request, pk):
    autor = get_object_or_404(Autor, id=pk)
    if request.method == "POST":
        autor.delete()
        messages.success(request, 'Autor eliminado exitosamente')
        return redirect("autor:autor_listar")
    return render(request, "autor/autor_delete.html", {"autor": autor})
