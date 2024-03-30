from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from cliente.forms import EnderecoForm, ClienteForm
from cliente.models import Cliente
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.hashers import check_password


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

def logout_cliente(request):
    logout(request)
    return redirect('home')  # direciona para a pagina inicial apor logout

def verificar_cadastro(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        if Cliente.objects.filter(email=email).exists():
            usuario = Cliente.objects.get(email=email)
            if(check_password(password = senha, encoded=usuario.senha)):
                return HttpResponse('Logado')
                #return render(request, 'cadastro_logado.html', {'usuarios': Cliente.objects.all()})
            else:
                return HttpResponse('Senha Incorreta')
        else: 
            return HttpResponse('Usuário não cadastrado')
    elif request.method=='GET' or 'email' in request.GET:
        email_busca = request.GET.get('email')
        usuario = Cliente.objects.filter(email__icontains=email_busca)
        return HttpResponse(usuario)    
    else:
        return HttpResponse('Método não permitido')
    
    
def excluir_cadastro(request, usuario_id):
    usuario = get_object_or_404(Cliente, pk=usuario_id)
    usuario.delete()
    return HttpResponse('Usuario excluido')
    #return render(request, 'cadastro_logado.html', {'usuarios': Cliente.objects.all()})
