from django.urls import path
from .views import listar_livros, detalhe_livro
from . import views
from django.http import HttpResponse

app_name = 'Livros'

urlpatterns = [
    path('', listar_livros),
    path('detalhe_livro/<int:id>/', detalhe_livro),  
]