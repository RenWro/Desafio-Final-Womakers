from django.shortcuts import render
from django.http import HttpResponse
from .forms import LivroForm
from .models import Livro
# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all()
    form = LivroForm(request.GET)

    return render(request, 'listar_livros.html',{'livros': livros,'form':form})
