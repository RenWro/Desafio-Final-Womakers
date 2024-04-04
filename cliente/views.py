from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from cliente.forms import EnderecoForm, ClienteForm
from cliente.models import Cliente
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def cadastrar_cliente(request):
    sucesso = False
    if request.method == 'POST':
        endereco_form = EnderecoForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if endereco_form.is_valid() and cliente_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            sucesso = True
    else:
        endereco_form = EnderecoForm()
        cliente_form = ClienteForm()
    contexto = {
        'endereco_form': endereco_form,
        'cliente_form': cliente_form,
        'sucesso': sucesso
    }
    return render(request, 'cadastro.html', contexto)


def login_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if Cliente.objects.filter(email=email).exists():
            cliente = Cliente.objects.get(email=email)
            if (check_password(password=senha, encoded=cliente.senha)):
                messages.success(request, 'Cliente logado com sucesso')
                return redirect('perfil')
            else:
                messages.error(request, 'Usuário ou senha incorretos')
        else:
            messages.error(request, 'Usuário ou senha incorretos')
        # usei render ao inves de redirect para panter os dados que o usuario escreveu na tela
        return render(request, 'login.html')
    return render(request, 'login.html')


@login_required(login_url="/cliente/login/")
def consultar_perfil(request):
    cliente = request.user
    return render(request, 'perfil.html', {'cliente': cliente})


@login_required(login_url="/cliente/login/")
def logout_cliente(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('/')


@login_required(login_url="/cliente/login/")
def excluir_cadastro(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()
    messages.success(request, 'Cadastro do cliente excluído com sucesso.')
    return redirect('/')
