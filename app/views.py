from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import LivroForm
from .models import Livro, Genero, Autores
from pedidos.models import Pedido

def main(request):
    return render(request, 'main.html')

def listar_livros(request):
    livros = Livro.objects.all()
    form = LivroForm(request.GET)
    generos = None
    autores = None

    if request.GET:            
        if 'id_genero' in request.GET:
            generos_ids = request.GET.getlist('id_genero')
            livros = livros.filter(generos__id__in=generos_ids)
            generos = Genero.objects.filter(id__in=generos_ids)
        if 'id_autor' in request.GET:
            autores_ids = request.GET.getlist('autores')
            livros = livros.filter(autores__id__in=autores_ids)
            autores = Autores.objects.filter(id__in=autores_ids)

    contexto = {
        'livros': livros,
        'form': form,
        'generos_atual': generos,
        'autores_atual': autores,
    }

    return render(request, 'listar_livros.html', contexto)


def listar_pedidos_cliente(request, cliente_id):
    # Filtra os pedidos do cliente e os ordena por data, da mais recente para a mais antiga
    pedidos = Pedido.objects.filter(cliente_id=cliente_id).order_by('-data_pedido')
    return render(request, 'listar_pedidos_cliente.html', {'pedidos': pedidos})

def detalhar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    return render(request, 'detalhes_pedido.html', {'pedido': pedido})