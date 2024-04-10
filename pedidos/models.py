from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.db.models.signals import pre_save, post_save, m2m_changed
from livro.models import Livro
from cliente.models import Cliente

# Mudar o user para cliente


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
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, null=True, blank=True)
    livros = models.ManyToManyField(Livro, blank=True)
    subtotal = models.DecimalField(
        default=0.00, max_digits=100, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    objects = GerenciadorCarrinho()

    def __str__(self):
        return str(self.id)


def modificacao_carrinho(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        livros = instance.livros.all()
        total = 0
        for livro in livros:
            total += livro.valor
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()


m2m_changed.connect(modificacao_carrinho, sender=Carrinho.livros.through)


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

    '''
    adicionar em Pedido:
        itens = models.ManyToManyField(Livro)

        pedido.itens.add(livro)

    acessar itens:
        pedido = Pedido.objects.get(pk=1)

        for livro in pedido.itens.all():
            print(livro.titulo)for livro in pedido.itens.all():

    '''

    def calcular_valor_total(self):
        valor_total = 0
        for item in self.itens_pedido.all():
            valor_total += item.valor_unitario * item.quantidade
        return valor_total
