from django import forms
from anuncio.models import Anuncio

class FormularioAnuncio(forms.ModelForm):
    class Meta:
        model = Anuncio
        exclude = []