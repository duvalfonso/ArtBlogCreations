from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ImagenForm, PublicacionForm
from .models import Imagen, Publicacion


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

        errores_imagenes = validar_imagenes(imagenes)

        if errores_imagenes:
            for error in errores_imagenes:
                form.add_error(None, error)

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

    def form_valid(self, form):
        imagenes = self.request.FILES.getlist("imagen")

        errores_imagenes = validar_imagenes(imagenes)

        if errores_imagenes:
            for error in errores_imagenes:
                form.add_error(None, error)

            return self.form_invalid(form)

        response = super().form_valid(form)

        for imagen in imagenes:
            self.object.imagenes.create(imagen=imagen)

        messages.success(self.request, "La publicación fue actualizada correctamente.")
        return response

    def get_success_url(self):
        return f"/publicaciones/{self.object.pk}/"


class PublicacionDeleteView(LoginRequiredMixin, DeleteView):
    model = Publicacion
    template_name = "publicaciones/eliminar.html"

    def get_queryset(self):
        return Publicacion.objects.filter(autor=self.request.user)

    def get_success_url(self):
        return "/publicaciones/"


class MisPublicacionesListView(LoginRequiredMixin, ListView):
    model = Publicacion
    template_name = "publicaciones/mis_publicaciones.html"
    context_object_name = "publicaciones"

    def get_queryset(self):
        return Publicacion.objects.filter(autor=self.request.user).order_by(
            "-fecha_publicacion"
        )


class ImagenDeleteView(LoginRequiredMixin, View):
    def post(self, request, pk):
        imagen = get_object_or_404(Imagen, pk=pk, publicacion__autor=request.user)
        publicacion = imagen.publicacion

        if publicacion.imagenes.count() <= 1:
            messages.error(request, "Una publicación debe tener al menos una imagen.")
            return redirect("editar_publicacion", pk=publicacion.pk)

        imagen.delete()
        messages.success(request, "La imagen fue eliminada correctamente.")
        return redirect("editar_publicacion", pk=publicacion.pk)


def validar_imagenes(imagenes):
    errores = []

    for imagen in imagenes:
        imagen_form = ImagenForm(files={"imagen": imagen})

        if not imagen_form.is_valid():
            errores.extend(imagen_form.errors.get("imagen", []))

    return errores
