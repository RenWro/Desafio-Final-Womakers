from django.shortcuts import render
from django.http import HttpResponse
from .forms import LivroForm
from .models import Livro, Genero, Autores

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