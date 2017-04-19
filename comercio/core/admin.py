from django.contrib import admin

from .models import Cliente
from .models import Venda
from .models import Produto
from .models import Fornecedor
from .models import Pedido
from .models import ItemVenda
from .models import ItemPedido

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('cpf', 'nome', 'email', 'telefone')

class VendaAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'data', 'valor')

class ProdutoAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nome', 'quantidade')

class FornecedorAdmin(admin.ModelAdmin):
	list_display = ('nome', 'website', 'telefone')

class PedidoAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'pedido', 'total')

class ItemVendaAdmin(admin.ModelAdmin):
	list_display = ('venda', 'produto', 'preco')

class ItemPedidoAdmin(admin.ModelAdmin):
	list_display = ('pedido', 'produto', 'preco')
		

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venda, VendaAdmin)
admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Fornecedor, FornecedorAdmin)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(ItemVenda, ItemVendaAdmin)
admin.site.register(ItemPedido, ItemPedidoAdmin)
