from django.db import models
from django.contrib.auth.models import User

class Pedido(models.Model):
    # id = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)

    # É UM CHOICE???????
    status = models.CharField(max_length=20, choices=[('pendente', 'Pendente'), ('aprovado', 'Aprovado'), ('cancelado', 'Cancelado')])
    
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=20)

    # criar uma lista com os produtos ?????? "itens_pedidos"


    def calcular_valor_total(self):
        valor_total = 0
        for item in self.itens_pedido.all():
            valor_total += item.valor_unitario * item.quantidade
        return valor_total

    def confirmar_pedido(self):
        self.status = 'aprovado'
        self.save()

    def cancelar_pedido(self):
        self.status = 'cancelado'
        self.save()

