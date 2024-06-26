from django.urls import path
from cliente.views import cadastrar_cliente, logout_cliente, login_cliente, excluir, consultar_perfil

app_name = 'Cliente'
urlpatterns = [
    path('cadastro/', cadastrar_cliente, name='cadastrar_cliente'),
    path('logout/', logout_cliente, name='logout_cliente'),
    path('login/', login_cliente, name='login_cliente'),
    path('perfil/', consultar_perfil, name='consultar_perfil'),
    path('excluir/', excluir, name='excluir'),
]
