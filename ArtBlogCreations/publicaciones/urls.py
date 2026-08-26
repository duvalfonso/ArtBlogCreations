from django.urls import path

from .views import (
    ImagenDeleteView,
    MisPublicacionesListView,
    PublicacionCreateView,
    PublicacionDeleteView,
    PublicacionDetailView,
    PublicacionListView,
    PublicacionUpdateView,
)

urlpatterns = [
    path(
        "",
        PublicacionListView.as_view(),
        name="lista_publicaciones",
    ),
    path(
        "mis-publicaciones/",
        MisPublicacionesListView.as_view(),
        name="mis_publicaciones",
    ),
    path(
        "crear/",
        PublicacionCreateView.as_view(),
        name="crear_publicacion",
    ),
    path(
        "imagenes/<int:pk>/eliminar/",
        ImagenDeleteView.as_view(),
        name="eliminar_imagen",
    ),
    path(
        "<int:pk>/",
        PublicacionDetailView.as_view(),
        name="detalle_publicacion",
    ),
    path(
        "<int:pk>/editar/",
        PublicacionUpdateView.as_view(),
        name="editar_publicacion",
    ),
    path(
        "<int:pk>/eliminar/",
        PublicacionDeleteView.as_view(),
        name="eliminar_publicacion",
    ),
]
