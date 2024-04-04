from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.


class Cliente (models.Model):
    cpf = models.CharField(max_length=11, primary_key=True, unique=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=13)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    senha = models.CharField(max_length=50)
    # pedidos = models.ManyToManyField(Pedido)  # Campo ManyToManyField, para completar precisa criar um models para pedidos.

    def criptografia(self, *args, **kwargs):
        self.senha = make_password(self.senha)
        super().save(**args, **kwargs)

    def __str__(self):
        return f'{self.nome}: {self.nome} - {self.cpf}'

    class Meta:
        verbose_name = 'Cadastro de cliente'
        verbose_name_plural = 'Cadastro de clientes'
        ordering = ['-data_cadastro']


class Endereco (models.Model):
    # Adicionando a chave estrangeira para Cliente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=10)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)

    def __str__(self):
        return self.cep
