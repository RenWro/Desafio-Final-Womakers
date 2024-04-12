from django.urls import path
from .views import *
# from django.http import HttpResponse

app_name = 'pedidos'
urlpatterns = [
    path('detalhes/<int:pedido_id>/', detalhar_pedido, name='detalhes_pedido'),
    path('finalizar/', finalizar_pedido, name='finalizar_pedido'),
    path('carrinho/', atualizar_carrinho, name='atualizar_carrinho'),
    path('detalhes_carrinho/', detalhes_carrinho, name='detalhes_carrinho'),
]
