#Questão 2

# a
cliente = Cliente(1, '600.451.623-60', 'Nome A', 'Endereco A', 'Complemento A', 'Cidade A', 'PI', '64000-000', '86 1111-1111', '86 2222-2222', 10000.00, 'emailclientea@email.com')
cliente.save()
# b
fornecedor = Fornecedor(1, '000000000000-00', 'Empresa B', 'Endereco B', 'Complemento B', 'Cidade B', 'PI', '64000-000', '86 3333-3333', 'Responsavel B', 'empresab.com')
fornecedor.save()
# c
produto = Produto(1, 'produto A', 5, 1.0)
produto.save()
# d
data = timezone.now()
pedido = Pedido(1, data, data + datetime.timedelta(days=1), 2000.00, 1)
pedido.save()
# e
itemPedido = ItemPedido(1, 1, 20.0, 2)
itemPedido.save()
# f
venda = Venda(1, data, 40.0, 1)
venda.save()
# g
itemVenda = ItemVenda(1, 1, 1, 20.0, 1)
itemVenda.save()

# Questão 3
# a
Cliente.objects.all()
# b
Venda.objects.filter(cliente_id = 1)
# c
Pedido.objects.get(id = 1)
# d
ItemPedido.objects.filter(pedido_id = 1)
# e
from django.db.models import F
Produto.objects.filter(quantidade__lte=F('minimo'))

