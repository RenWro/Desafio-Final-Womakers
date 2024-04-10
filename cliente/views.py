from django.shortcuts import render
from cliente.forms import ClienteForm, EnderecoFormSet
from cliente.models import Cliente
from django.contrib.auth import logout, login
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def cadastrar_cliente(request):
    sucesso = False
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        endereco_formset = EnderecoFormSet(request.POST)
        if endereco_formset.is_valid() and cliente_form.is_valid():
            cliente = cliente_form.save()
            endereco_formset.instance = cliente
            endereco_formset.save()
            sucesso = True
            messages.success(request, 'Cadastro efetuado com sucesso')
        else:
            messages.error(
                request, 'Erro no cadastro.')
    endereco_formset = EnderecoFormSet()
    cliente_form = ClienteForm()
    contexto = {
        'endereco_formset': endereco_formset,
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
            if (check_password(password=senha, encoded=cliente.password)):
                login(request=request, user=cliente)
                messages.success(request, 'Cliente logado com sucesso')
                return redirect('/cliente/perfil/')
            else:
                messages.error(request, 'Usuário ou senha incorretos')
        else:
            messages.error(request, 'Usuário ou senha incorretos')

    return render(request, 'login.html')


@login_required(login_url="/cliente/login/")
def consultar_perfil(request):
    print(request)
    cliente = request.user
    return render(request, 'perfil.html', {'cliente': cliente})


@login_required(login_url="/cliente/login/")
def logout_cliente(request):
    logout(request)
    messages.success(request, 'Logout realizado com sucesso.')
    return redirect('/')


@login_required(login_url="/cliente/login/")
def excluir(request):
    cliente = request.user
    cliente.delete()
    messages.success(request, 'Cadastro excluído com sucesso.')
    return redirect('/')


# @login_required(login_url="/cliente/login/")
# def excluir_cadastro(request, cliente_id):
#     cliente = get_object_or_404(Cliente, pk=cliente_id)
#     cliente.delete()
#     messages.success(request, 'Cadastro do cliente excluído com sucesso.')
#     return redirect('/')
