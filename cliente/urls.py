from django.urls import path
from cliente.views import cadastrar_cliente

app_name = 'Cliente'
urlpatterns = [
    path('cadastro/', cadastrar_cliente, name='cadastrar_cliente')
]