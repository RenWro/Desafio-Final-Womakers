from django.urls import path
from app.views import listar_livros, detalhes_pedido, listar_pedidos_cliente
# from django.http import HttpResponse

app_name= 'Livros'
urlpatterns = [
    path('', listar_livros),
    # to achando que esse é o local errado mas  fiz aqui por enquanto
    path('pedido/<int:pedido_id>/', detalhes_pedido, name='detalhes_pedido'),
    path('cliente/<int:cliente_id>/pedidos/', listar_pedidos_cliente, name='listar_pedidos_cliente'),
]