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
        labels = {
            'cpf':'CPF',
            'nome':'Nome',
            'email':'E-mail',
            'telefone':'Telefone',
            'senha':'Senha'
        }
    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['senha'].required = True

EnderecoFormSet = inlineformset_factory(
    Cliente, Endereco, max_num=1, 
    fields=('rua', 'numero', 'complemento', 'cidade', 'estado', 'cep'),
    labels = {
            'rua': 'Rua',
            'numero': 'Número',
            'complemento': 'Complemento',
            'cidade': 'Cidade',
            'estado':'Estado',
            'cep':'CEP'
        })