from django.contrib import admin
from .models import Genero, Autores, Livro, Usuario, Pedidos

class GeneroAdmin(admin.ModelAdmin):
  list_display = ["nome"]

class AutoresAdmin(admin.ModelAdmin):
  list_display = ["nome", "sobrenome"]
  search_fields = ['nome']
  list_filter = ['nome']

class LivroAdmin(admin.ModelAdmin):
  list_display = ['isbn', 'titulo', 'valor', 'estoque', 'descricao', 'editora', 'id_genero']
  search_fields = ['titulo', 'descricao', 'editora']
  list_filter = ['isbn']

class UsuarioAdmin(admin.ModelAdmin):
  list_display = ["nome","sobrenome","endereco","email","telefone","cpf"]
  search_fields = ['nome', 'endereco', 'email', 'cpf']
  list_filter = ['sobrenome']

class PedidosAdmin(admin.ModelAdmin):
  list_display = ["data","status","usuario"]
  search_fields = ['usuario']
  list_filter = ['data']

admin.site.register(Genero, GeneroAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Autores, AutoresAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Pedidos, PedidosAdmin)
