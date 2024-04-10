from typing import Any, Mapping
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Livro, Genero, Autores

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields= '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        generos = Genero.objects.all()
        autores = Autores.objects.all()
        self.fields['id_genero'].queryset = generos
        self.fields['autores'].queryset = autores

class AutoresForm(forms.ModelForm):
    class Meta:
        model = Autores
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)