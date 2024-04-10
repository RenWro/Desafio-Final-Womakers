from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .forms import LivroForm, AutoresForm
from .models import Livro, Genero, Autores, Editora
from django.views.generic import ListView, DetailView


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
    instance = get_object_or_404(Livro, id=id)
    instance_autor = get_object_or_404(Autores, id=id)
    instance_editora = get_object_or_404(Editora, id=id)
    instance_genero = get_object_or_404(Genero, id=id)
    form_livro = LivroForm(request.GET)

    context = {
        'livro': instance,
        'autor': instance_autor,
        'editora': instance_editora,
        'genero': instance_genero,
        'form_livro': form_livro,
    }
    return render(request, "detalhe_livro.html", context)

def serve_imagem(request, livro_id):
    livro = get_object_or_404(Livro, id=livro_id)
    if livro.imagem_capa:
        return HttpResponse(livro.imagem_capa, content_type='image/jpeg')
    else:
        return HttpResponse(status=404)