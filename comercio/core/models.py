from django.db import models

from datetime import datetime

class Cliente(models.Model):
	cpf = models.CharField(max_length=14, primary_key=True)
	nome = models.CharField(max_length=30)
	endereco = models.CharField(max_length=35)
	complemento = models.CharField(max_length=50)
	cidade = models.CharField(max_length=25)
	estado = models.CharField(max_length=2)
	cep = models.CharField(max_length=8)
	telefone = models.CharField(max_length=15)
	celular = models.CharField(max_length=15)
	renda = models.DecimalField(max_digits=10, decimal_places=2)
	email = models.EmailField(max_length=50)

	def __str__(self):
		return self.nome

class Venda(models.Model):
	codigo = models.AutoField(primary_key=True)
	data = models.DateTimeField(default=datetime.now, blank=True)
	valor =  models.DecimalField(max_digits=10, decimal_places=2)
	cliente = models.ForeignKey('Cliente')

class Produto(models.Model):
	codigo = models.IntegerField(default=0, primary_key=True)
	nome = models.CharField(max_length=35)
	quantidade = models.IntegerField(default=0)
	minimo = models.DecimalField(max_digits=10, decimal_places=2)

class Fornecedor(models.Model):
	cnpj = models.CharField(max_length=20, primary_key=True)
	nome = models.CharField(max_length=30)
	endereco = models.CharField(max_length=35)
	complemento = models.CharField(max_length=50)
	cidade = models.CharField(max_length=25)
	estado = models.CharField(max_length=2)
	cep = models.CharField(max_length=8)
	telefone = models.CharField(max_length=15)
	responsavel = models.CharField(max_length=30)
	website = models.CharField(max_length=80)

class Pedido(models.Model):
	codigo = models.IntegerField(default=0, primary_key=True)
	pedido = models.DateTimeField(default=datetime.now, blank=True)
	recebimento = models.DateTimeField()
	total =  models.DecimalField(max_digits=10, decimal_places=2)
	fornecedor = models.ForeignKey('Fornecedor')

class ItemVenda(models.Model):
	venda = models.ForeignKey('Venda')
	produto = models.ForeignKey('Produto')
	preco = models.DecimalField(max_digits=10, decimal_places=2)
	quantidade = models.IntegerField(default=0)

class ItemPedido(models.Model):
	pedido = models.ForeignKey('Pedido')
	produto = models.ForeignKey('Produto')
	preco = models.DecimalField(max_digits=10, decimal_places=2)
	quantidade = models.IntegerField(default=0)

	

