from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save, m2m_changed
from django.conf import settings
from decimal import Decimal
from livro.models import Livro
from cliente.models import Cliente

class GerenciadorCarrinho(models.Manager):
    def novo_ou_existente(self, request):
        carrinho_id = request.session.get("carrinho_id", None)
        consultas = self.get_queryset().filter(id=carrinho_id)
        if consultas.count() == 1:
            novo = False
            livro_carrinho = consultas.first()
            if request.user.is_authenticated and livro_carrinho.user is None:
                livro_carrinho.user = request.user
                livro_carrinho.save()
        else:
            livro_carrinho = Carrinho.objects.new(user=request.user)
            novo = True
            request.session['carrinho_id'] = livro_carrinho.id
        return livro_carrinho, novo

    def novo(self, user=None):
        cliente = None
        if user is not None:
            if user.is_authenticated:
                cliente = user
        return self.model.objects.create(user=cliente)

class Carrinho(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    livros = models.ManyToManyField(Livro, through='ItemCarrinho')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def pre_salvar_carrinho(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal)
    else:
        instance.total = 0.00

pre_save.connect(pre_salvar_carrinho, sender=Carrinho)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_pedido = models.DateTimeField(auto_now_add=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pagamento = models.CharField(max_length=20)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)

    def calcular_valor_total(self):
        valor_total = 0
        for item in self.itens_pedido.all():
            valor_total += item.valor_unitario * item.quantidade
        return valor_total