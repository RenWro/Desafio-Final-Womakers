from django.urls import path
from cliente.views import cadastrar_cliente, logout_cliente, verificar_cadastro, excluir_cadastro

app_name = 'Cliente'
urlpatterns = [
    path('cadastro/', cadastrar_cliente, name='cadastrar_cliente'),
    path('logout/', logout_cliente, name='logout_cliente'),
    path('verificar_cadastro/', verificar_cadastro, name='verificar_cadastro'),
    path('excluir_cadastro/<int:usuario_id>', excluir_cadastro, name='excluir_cadastro')
]