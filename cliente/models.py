from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Cliente(AbstractUser):
    cpf = models.CharField(max_length=11, null=True, blank=True)
    nome = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, unique=True)
    telefone = models.CharField(max_length=13, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name=('groups'),
    #     blank=True,
    #     related_name='cliente_groups',
    #     related_query_name='cliente',
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=('user permissions'),
    #     blank=True,
    #     related_name='cliente_user_permissions',
    #     related_query_name='cliente',
    # )

    def save(self, *args, **kwargs):
        self.username = self.email
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nome}: {self.nome} - {self.cpf}'

    class Meta:
        verbose_name = 'Cadastro de cliente'
        verbose_name_plural = 'Cadastro de clientes'
        ordering = ['-data_cadastro']


class Endereco (models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    rua = models.CharField(max_length=100, null=True, blank=True)
    numero = models.IntegerField(null=True, blank=True)
    complemento = models.CharField(max_length=10, null=True, blank=True)
    cidade = models.CharField(max_length=20, null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    cep = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.cep
