from django.shortcuts import render

from app.models import Livro
# Create your views here.

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'listar_livros.html',{'livros': livros})
