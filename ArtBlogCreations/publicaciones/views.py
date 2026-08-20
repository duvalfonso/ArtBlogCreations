from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import PublicacionForm
from .models import Publicacion


class PublicacionListView(ListView):
    model = Publicacion
    template_name = "publicaciones/lista.html"
    context_object_name = "publicaciones"

    ordering = ["-fecha_publicacion"]


class PublicacionDetailView(DetailView):
    model = Publicacion
    template_name = "publicaciones/detalle.html"
    context_object_name = "publicacion"


class PublicacionCreateView(LoginRequiredMixin, CreateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = "publicaciones/crear.html"

    def form_valid(self, form):
        imagenes = self.request.FILES.getlist("imagen")

        if not imagenes:
            form.add_error(None, "Debes seleccionar al menos una imagen.")
            return self.form_invalid(form)

        form.instance.autor = self.request.user
        response = super().form_valid(form)

        for imagen in imagenes:
            self.object.imagenes.create(imagen=imagen)

        messages.success(self.request, "La publicacion fue creada correctamente.")

        return response

    def get_success_url(self):
        return f"/publicaciones/{self.object.pk}/"


class PublicacionUpdateView(LoginRequiredMixin, UpdateView):
    model = Publicacion
    form_class = PublicacionForm
    template_name = "publicaciones/editar.html"

    def get_queryset(self):
        return Publicacion.objects.filter(autor=self.request.user)

    def get_success_url(self):
        return f"/publicaciones/{self.object.pk}/"


class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = "publicaciones/eliminar.html"

    def get_queryset(self):
        return Publicacion.objects.filter(autor=self.request.user)

    def get_success_url(self):
        return "/publicaciones/"
