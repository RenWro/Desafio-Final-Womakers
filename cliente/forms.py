from django import forms
from django.forms import inlineformset_factory
from cliente.models import Cliente, Endereco
from django.contrib.auth.hashers import make_password


class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['rua', 'numero', 'complemento', 'cidade', 'estado', 'cep']


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'email', 'telefone', 'password']
        widgets = {'password': forms.PasswordInput()}
        labels = {
            'cpf': 'CPF',
            'nome': 'Nome',
            'email': 'E-mail',
            'telefone': 'Telefone',
            'password': 'Senha'
        }

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['password'].required = True

    def save(self, commit=True):
        cliente = super(ClienteForm, self).save(commit=False)
        cliente.password = make_password(self.cleaned_data['password'])
        if commit:
            cliente.save()
        return cliente


EnderecoFormSet = inlineformset_factory(
    Cliente, Endereco, max_num=1,
    can_delete=False,
    fields=('rua', 'numero', 'complemento', 'cidade', 'estado', 'cep'),
    labels={
        'rua': 'Rua',
        'numero': 'Número',
        'complemento': 'Complemento',
        'cidade': 'Cidade',
        'estado': 'Estado',
        'cep': 'CEP'
    })
