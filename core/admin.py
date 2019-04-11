from django.contrib import admin

from .models import *


class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'cod_cliente', 'nome_cliente', 'rg_cliente', 'telefone_cliente', 'endereco_cliente'
    )

class VendaAdmin(admin.ModelAdmin):
    list_display = (
        'cod_venda', 'cod_cliente', 'data_venda', 'valor_venda'
    )

class ProdutoAdmin(admin.ModelAdmin):
    list_display = (
        'cod_produto', 'nome_produto', 'valor_produto', 'qnt_estoque'
    )



admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Itens)