from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.contrib import messages
from .forms import LivroForm
from .models import Livro, Genero, Autores
from pedidos.models import Carrinho, Pedido, CarrinhoLivro
from cliente.models import Cliente


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
    return render(request, 'lista_livros.html', contexto)


def detalhe_livro(request, id=None):
    try:
        instance = get_object_or_404(Livro, id=id)
    except Http404:
        messages.error(request, f'Livro com id={id} não localizado')
        return redirect('/livro/')

    form_livro = LivroForm(request.GET)
    context = {
        'livro': instance,
        'form_livro': form_livro,
    }
    return render(request, "detalhe_livro.html", context)


def adicionar_ao_carrinho(request):
    livro_id = request.POST['livro_id']
    quantidade = request.POST['quantidade']
    cliente = request.user
    carrinho = Carrinho()
    carrinho.add_item_carrinho(
        cliente_id=cliente.id, livro_id=livro_id, quantidade=quantidade)

    messages.success(request, 'Livro adicionado ao carrinho')
    return redirect(f'/livro/detalhe_livro/{livro_id}')
