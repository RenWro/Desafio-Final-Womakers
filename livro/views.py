from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import LivroForm
from .models import Livro, Genero, Autores
from pedidos.models import Carrinho, Pedido, CarrinhoLivro


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


@login_required
def adicionar_ao_carrinho(request):
    if request.user.is_authenticated:
        livro_id = request.POST.get('livro_id')
        quantidade = int(request.POST.get('quantidade'))
        cliente = request.user
        carrinho = Carrinho()
        msg_retorno = carrinho.add_item_carrinho(
            cliente_id=cliente.id, livro_id=livro_id, quantidade=quantidade)

        if msg_retorno == True:
            messages.success(request, 'Livro adicionado ao carrinho')
        else:
            messages.error(request, msg_retorno)

        return redirect(f'/livro/detalhe_livro/{livro_id}')
    else:
        return redirect('/')


def search_view(request):
    query = request.GET.get('q')
    results = None

    if query:
        results = Livro.objects.filter(titulo__icontains=query)

    return render(request, 'search_results.html', {'query': query, 'results': results})
