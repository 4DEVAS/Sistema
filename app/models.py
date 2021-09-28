from django.db import models

# Criando a tabela Empresa
class Empresa(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    ramo = models.CharField(max_length=100)

# Criando a tabela Produto
class Produto(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=150)
    descricao = models.CharField(max_length=200)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    empresa = models.ForeignKey('Empresa',on_delete=models.CASCADE)



