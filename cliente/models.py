from django.db import models

# Create your models here.

class Endereco (models.Model):
    rua = models.CharField(max_length=100)
    numero = models.IntegerField()
    complemento = models.CharField(max_length=10)
    cidade = models.CharField(max_length=20)
    estado = models.CharField(max_length=20)
    cep = models.CharField(max_length=10)
    def __str__(self):
        return self.cep

class Cliente (models.Model):
    cpf = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=13)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE)
    senha = models.CharField(max_length=50)
    # pedidos = models.ManyToManyField(Pedido)  # Campo ManyToManyField, para completar precisa criar um models para pedidos. 
    def __str__(self):
        return f'{self.nome}: {self.nome} - {self.cpf}'
    class Meta: 
        verbose_name = 'Cadastro de usuário'
        verbose_name_plural = 'Cadastro de usuários'
        ordering = ['-data_cadastro']


