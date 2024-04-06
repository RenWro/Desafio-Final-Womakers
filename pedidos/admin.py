from django.contrib import admin
from .models import Pedido


class PedidosAdmin(admin.ModelAdmin):
    list_display = ['cliente', 'data_pedido', 'valor_total', 'forma_pagamento']
    search_fields = ['cliente']
    list_filter = ['data_pedido']


admin.site.register(Pedido, PedidosAdmin)
