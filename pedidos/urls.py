from django.urls import path
from .views import *
# from django.http import HttpResponse

app_name = 'Pedido'
urlpatterns = [
    path('detalhes/<int:pedido_id>/', detalhar_pedido, name='detalhes_pedido'),
    path('finalizar/<int:cliente_id>/',
         finalizar_pedido, name='finalizar_pedido'),
    path('detalhes_carrinho/', detalhes_carrinho, name='detalhes_carrinho'),
    path('excluir_item_carrinho/', excluir_item_carrinho,
         name='excluir_item_carrinho')
]
