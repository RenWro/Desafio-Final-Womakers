from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.conf import settings
from decimal import Decimal
from livro.models import Livro
from cliente.models import Cliente
from enumfields import EnumField
from enum import Enum


#    /* ------Enum Fields ----- */


class StatusPedido(Enum):
    PENDENTE = 'PagamentoPendente'
    CONFIRMADO = 'Pagamento Confirmado'
    CAMINHO = 'A caminho'
    ENTREGUE = 'Entregue'


class FormaPagamento(Enum):
    PIX = 'Pix'
    CREDITO = 'Cartão de crétido'
    DEBITO = 'Cartão de débito'

#    /* ----------------------- */


class Carrinho(models.Model):
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE)
    # livros = models.ManyToManyField(Livro)

    def add_item_carrinho(self, cliente_id, livro_id, quantidade=1):
        livro = Livro.objects.get(pk=livro_id)
        cliente = Cliente.objects.get(pk=cliente_id)

        # Verifica se o cliente já tem um carrinho
        carrinho = cliente.carrinho_set.first()
        if not carrinho:
            carrinho = Carrinho.objects.create(cliente=cliente)
            carrinho.save()

        # Verifica se o livro já está no carrinho
        carrinho_livro, created = CarrinhoLivro.objects.get_or_create(
            carrinho=carrinho, livro=livro)
        if not created:
            carrinho_livro.quantidade += int(quantidade)
        else:
            carrinho_livro.quantidade = quantidade
        carrinho_livro.save()

    def atualizar_quantidade(self, livro, nova_quantidade=1):
        print('atualizarQuantidade()')
        pass

    def ver_detalhes(self):
        detalhes = []
        for item in self.carrinholivro_set.all():
            detalhes.append({
                'titulo': item.livro.titulo,
                'quantidade': item.quantidade,
                'valor': item.livro.valor,
                # 'subtotal': item.quantidade * item.livro.preco
            })
        return detalhes

    def finaliza_pedido(self):
        print('finalizarPedido()')
        pass


# Classe que relaciona a quantidade de livros a classe Livros
class CarrinhoLivro(models.Model):
    carrinho = models.ForeignKey(
        Carrinho, on_delete=models.CASCADE, null=True, blank=True)
    livro = models.ForeignKey(
        Livro, on_delete=models.CASCADE, null=True, blank=True)
    quantidade = models.PositiveIntegerField(default=1, null=True, blank=True)
    data_hora_item_criado = models.DateTimeField(auto_now_add=True)
    data_hora_item_atualizado = models.DateTimeField(auto_now=True)


class Pedido(models.Model):  #
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=20)
    status = EnumField(StatusPedido, max_length=20,
                       default=StatusPedido.PENDENTE)
    forma_de_pagamento = EnumField(
        FormaPagamento, max_length=20, default=FormaPagamento.CREDITO)

    def calcular_valor_total(self):
        valor_total = 0
        for item in self.itens_pedido.all():
            valor_total += item.valor_unitario * item.quantidade
        return valor_total

    def finalizar_pedido(self):
        print('finalizar_pedido()')
        pass
