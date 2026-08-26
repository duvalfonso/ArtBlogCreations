from django.contrib import admin

from .models import Imagen, Publicacion


class ImagenInLine(admin.TabularInline):
    model = Imagen
    extra = 0
    fields = ("imagen",)


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

    ordering = ("-fecha_publicacion",)

    readonly_fields = ("fecha_publicacion",)

    list_per_page = 20

    inlines = [
        ImagenInLine,
    ]


@admin.register(Imagen)
class ImagenAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "publicacion",
        "imagen",
    )

    search_fields = (
        "publicacion__titulo",
        "publicacion__autor__username",
    )

    list_filter = ("publicacion",)


admin.site.site_header = "ArtBlog Creations"
admin.site.site_title = "ArtBlog Creations"
admin.site.index_title = "Administración del sitio"
