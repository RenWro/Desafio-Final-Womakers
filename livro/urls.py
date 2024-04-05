from django.urls import path
from .views import listar_livros
from . import views
from django.http import HttpResponse

app_name= 'Livros'

urlpatterns = [
    path('', listar_livros),
    path('', views.listar_livros),
]