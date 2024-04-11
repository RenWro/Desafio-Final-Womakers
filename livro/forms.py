from django import forms
from .models import Livro, Genero, Autores

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        generos = Genero.objects.all()
        autores = Autores.objects.all()
        self.fields['id_genero'].queryset = generos
        self.fields['autores'].queryset = autores