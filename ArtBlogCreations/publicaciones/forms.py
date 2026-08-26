from django import forms

from .models import Imagen, Publicacion


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = [  # noqa: RUF012
            "titulo",
            "descripcion",
            "tipo",
        ]

        widgets = {  # noqa: RUF012
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Título de la obra",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Describe la obra",
                    "rows": 5,
                }
            ),
            "tipo": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),
        }

    def clean_titulo(self):
        titulo = self.cleaned_data["titulo"].strip()

        if len(titulo) < 3:
            raise forms.ValidationError("El título debe tener al menos 3 caracteres.")
        return titulo

    def clean_descripcion(self):
        descripcion = self.cleaned_data["descripcion"].strip()

        if len(descripcion) < 10:
            raise forms.ValidationError(
                "La descripción debe tener al menos 10 caracteres."
            )
        return descripcion


class ImagenForm(forms.ModelForm):
    imagen = forms.ImageField(
        error_messages={
            "invalid_image": (
                "El archivo seleccionado no es una imagen válida o está dañado."
            ),
            "invalid": ("El archivo seleccionado no es una imagen válida."),
            "required": "Debes seleccionar una imagen.",
        }
    )

    class Meta:
        model = Imagen
        fields = [
            "imagen",
        ]
        widgets = {
            "imagen": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                }
            ),
        }

    def clean_imagen(self):
        imagen = self.cleaned_data["imagen"]

        tipos_permitidos = [
            "image/jpeg",
            "image/png",
            "image/webp",
        ]

        if imagen.content_type not in tipos_permitidos:
            raise forms.ValidationError("Solo se permiten imágenes JPG, PNG o WEBP.")

        max_size = 10 * 1024 * 1024

        if imagen.size > max_size:
            raise forms.ValidationError("La imagen no puede superar los 10 MB.")

        return imagen
