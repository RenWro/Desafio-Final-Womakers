from django.contrib import admin
from .models import Genero, Autores, Livro


class GeneroAdmin(admin.ModelAdmin):
    list_display = ["nome"]


class AutoresAdmin(admin.ModelAdmin):
    list_display = ["nome", "sobrenome"]
    search_fields = ['nome']
    list_filter = ['nome']


class LivroAdmin(admin.ModelAdmin):
    list_display = ['isbn', 'titulo', 'valor',
                    'estoque', 'descricao', 'editora', 'id_genero']
    search_fields = ['titulo', 'descricao', 'editora']
    list_filter = ['isbn']


admin.site.register(Genero, GeneroAdmin)
admin.site.register(Autores, AutoresAdmin)
admin.site.register(Livro, LivroAdmin)
