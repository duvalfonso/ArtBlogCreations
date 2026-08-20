from django import forms

from .models import Publicacion


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
                    "class": "form-control",
                }
            ),
        }
