from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from cliente.forms import EnderecoForm, ClienteForm
from cliente.models import Cliente
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required

# Create your views here.


def cadastrar_cliente(request):
    sucesso = False
    if request.method == 'POST':
        endereco_form = EnderecoForm(request.POST)
        cliente_form = ClienteForm(request.POST)
        if endereco_form.is_valid() and cliente_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco  # Associando o endereço ao cliente
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
    return HttpResponse(cliente_form.as_p() + endereco_form.as_p())
#    return render(request, 'cadastro.html', contexto)


def login_cliente(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if Cliente.objects.filter(email=email).exists():
            cliente = Cliente.objects.get(email=email)
            if (check_password(password=senha, encoded=cliente.senha)):
                return HttpResponse('Logado')
                # return render(request, 'login.html', {'cliente': Cliente.objects.all()})
            else:
                return HttpResponse('Senha Incorreta')
        else:
            return HttpResponse('Usuário não cadastrado')
    # acho que essa linha é inutil pr a funcao consultar_perfil faz a mesma coisa
    elif request.method == 'GET' or 'email' in request.GET:
        #email_busca = request.GET.get('email')
        #cliente = Cliente.objects.filter(email__icontains=email_busca)
        #return HttpResponse('login')  # (cliente)
         return render(request, 'login.html')
    else:
        return HttpResponse('Método não permitido')


@login_required  # (login_url="/cliente/login/")
def consultar_perfil(request):
    cliente = request.user
    return render(request, 'perfil.html', {'cliente': cliente})


@login_required  # (login_url="/cliente/login/")
def logout_cliente(request):
    logout(request)
    return redirect('')  # direciona para a pagina inicial apos logout


@login_required  # (login_url="/cliente/login/")
def excluir_cadastro(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    cliente.delete()
    return HttpResponse('Cadastro do cliente excluido')
    # return render(request, 'home.html', {'cliente': Cliente.objects.all()})
