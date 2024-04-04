from django.urls import path
from . import views
from django.http import HttpResponse

app_name= 'Livros'
urlpatterns = [
    path('', views.listar_livros)
]