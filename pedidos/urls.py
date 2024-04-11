from django.urls import path
from .views import *
# from django.http import HttpResponse

app_name = 'Pedido'
urlpatterns = [
    path('detalhes/<int:pedido_id>/', detalhar_pedido, name='detalhes_pedido'),
    path('finalizar/<int:cliente_id>/',
         finalizar_pedido, name='finalizar_pedido'),
    path('carrinho/', atualizar_carrinho, name='atualizar_carrinho'),
    path('detalhes_carrinho/', detalhar_carrinho, name='detalhes_carrinho'),
]
