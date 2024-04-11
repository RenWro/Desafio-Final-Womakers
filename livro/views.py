from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404, JsonResponse
from django.contrib import messages
from .forms import LivroForm
from .models import Livro, Genero, Autores
from pedidos.models import Carrinho, ItemCarrinho

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
    if request.method == 'POST' and request.is_ajax():
        livro_id = request.POST.get('livro_id')
        livro = get_object_or_404(Livro, id=livro_id)        
        carrinho, cria = Carrinho.objects.novo_ou_existente(request)
        livro_carrinho, novo_livro = ItemCarrinho.objects.get_or_create(carrinho=carrinho, livro=livro)
        
        if not novo_livro:
            livro_carrinho.quantidade += 1 
            livro_carrinho.save()

        return JsonResponse({'success': True})    
    return JsonResponse({'error': 'Invalid request'})