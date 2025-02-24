from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from apps.libro.forms import LibroForm
from apps.libro.models import Libro
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# funciones.
def index (request):
    return render(request, "dashboard.html")

def libro_create(request):
    if request.method == "POST":
        form = LibroForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro creado exitosamente')
            return redirect("libro:libro_listar")
        else:
            messages.info(request, 'Existen campos faltantes o incorrectos')
    else:
        form = LibroForm()
    return render(request, "libro/libro_form.html", {"form": form})

class LibroCreate(SuccessMessageMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro/libro_form.html"
    success_url = reverse_lazy("libro:libro_listar")

    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Libro creado exitosamente")
        return super().form_valid(form)

def libro_list(request):
    libros_list = Libro.objects.all()
    find = request.GET.get('find', '') 
    
    # Si se proporciona un término de búsqueda
    if find:
        libros_list = libros_list.filter(titulo__icontains=find) 
    
    # Paginación
    paginator = Paginator(libros_list, 2)
    page = request.GET.get('page')

    try:
        libros = paginator.page(page)
    except PageNotAnInteger:
        libros = paginator.page(1)
    except EmptyPage:
        libros = paginator.page(paginator.num_pages)

    # Renderizamos la respuesta
    return render(request, 'libro/libro_list.html', {'libros': libros})

class LibroList(ListView):
    model = Libro
    template_name = 'libro/libro_listar.html'
    context_object_name = 'libros'

    def get_queryset(self):
        queryset = super().get_queryset() 
        find = self.request.GET.get('find', '')
        if find:
            queryset = queryset.filter(titulo__icontains=find)
        return queryset

def libro_edit(request, pk):
    libro = get_object_or_404(libro, id=pk)
    if request.method == "GET":
        form = LibroForm(instance=libro)
    else:
        form = LibroForm(request.POST, request.FILES, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado exitosamente')
            return redirect("libro:libro_listar")
        else:
            messages.info(request, 'Existen campos faltantes o incorrectos')
    return render(request, "libro/libro_form.html", {"form": form})

class LibroUpdate(SuccessMessageMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "libro/libro_form.html"
    success_url = reverse_lazy("libro:libro_listar")

    def form_invalid(self, form):
        messages.info(self.request, "Existen campos faltantes o incorrectos")
        return super().form_invalid(form)

    def form_valid(self, form):
        messages.success(self.request, "Libro actualizado exitosamente")
        return super().form_valid(form)

def libro_delete(request, pk):
    libro = get_object_or_404(libro, id=pk)
    if request.method == "POST":
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente')
        return redirect("libro:libro_listar")
    return render(request, "libro/libro_delete.html", {"libro": libro})

class LibroDelete(DeleteView):
    model = Libro
    template_name = "libro/libro_delete.html"
    success_url = reverse_lazy("libro:libro_listar")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Libro eliminado exitosamente")
        return super().delete(request, *args, **kwargs)


