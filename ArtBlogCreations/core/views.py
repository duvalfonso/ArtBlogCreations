from django.shortcuts import render
from publicaciones.models import Publicacion


def inicio(request):
    publicaciones = Publicacion.objects.all().order_by("-fecha_publicacion")[:3]
    return render(request, "core/inicio.html", {"publicaciones": publicaciones})
