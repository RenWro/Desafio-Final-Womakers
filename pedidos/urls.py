from django.urls import path
from .views import *
# from django.http import HttpResponse

app_name= 'Pedido'
urlpatterns = [
    path('detalhar/<int:pedido_id>/', detalhar_pedido, name='detalhar_pedido'),
    path('finalizar/<int:cliente_id>/', finalizar_pedido, name='finalizar_pedido'),
]