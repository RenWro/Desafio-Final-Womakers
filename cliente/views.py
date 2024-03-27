from django.shortcuts import render
from django.http import HttpResponse
from cliente.forms import EnderecoForm, ClienteForm

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
