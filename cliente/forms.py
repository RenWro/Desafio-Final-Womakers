from django import forms
from django.forms import inlineformset_factory
from cliente.models import Cliente, Endereco


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'cidade', 'estado', 'cep']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'email', 'telefone', 'senha']
        widgets = {'senha': forms.PasswordInput()}


EnderecoFormSet = inlineformset_factory(
    Cliente, Endereco, fields=('rua', 'numero', 'complemento', 'cidade', 'estado', 'cep'))
