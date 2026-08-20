from django.contrib import admin

from .models import Imagen, Publicacion


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "autor",
        "tipo",
        "fecha_publicacion",
    )

    list_filter = (
        "tipo",
        "fecha_publicacion",
    )

    search_fields = (
        "titulo",
        "descripcion",
        "autor__username",
    )


@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = (
        "publicacion",
        "imagen",
    )
