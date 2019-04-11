from django.db import models

class Cliente(models.Model):
    cod_cliente = models.AutoField(primary_key=True)
    nome_cliente = models.CharField(max_length=40)
    rg_cliente = models.CharField(max_length=7)
    telefone_cliente = models.CharField(max_length=11)
    endereco_cliente = models.TextField()

    def __str__(self):

        return self.nome_cliente

class Venda(models.Model):
    cod_venda = models.AutoField(primary_key=True)
    cod_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_venda = models.DateField()
    valor_venda = models.FloatField()

    def __str__(self):
        return self.cod_venda

class Produto(models.Model):
    cod_produto = models.AutoField(primary_key=True)
    nome_produto = models.CharField(max_length=30)
    valor_produto = models.FloatField()
    qnt_estoque = models.IntegerField()

    def __str__(self):
        return self.nome_produto


class Itens(models.Model):
    cod_produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cod_venda = models.ForeignKey(Venda, on_delete=models.CASCADE)
    qnt_produto = models.IntegerField()

    def __int__(self):
        return self.cod_venda