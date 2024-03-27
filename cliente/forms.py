from django import forms
from cliente.models import Cliente, Endereco
from datetime import date, time

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'cidade', 'estado', 'cep']

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'email', 'telefone', 'endereco', 'senha']
