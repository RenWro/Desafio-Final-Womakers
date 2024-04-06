from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nome",
                    "endereco", "email", "telefone", "cpf"]
    search_fields = ['nome', 'endereco', 'email', 'cpf']
    list_filter = ['email']


admin.site.register(Cliente, ClienteAdmin)
