from django.urls import path
from app.views import listar_livros
from django.http import HttpResponse

app_name= 'Livros'
urlpatterns = [
    path('', listar_livros)

]