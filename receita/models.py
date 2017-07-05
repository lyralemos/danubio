from decimal import Decimal

from django.db import models

from produto.models import Produto

class Receita(models.Model):
    produto = models.ForeignKey(Produto)
    descricao = models.TextField('Descrição')
    ingredientes = models.ManyToManyField('Ingrediente', through='IngredienteReceita')
    rendimento = models.IntegerField()

    def ingredientes_count(self):
        return self.ingredientereceita_set.count()
    ingredientes_count.short_description = 'Quantidade de Ingredientes'

    def custo(self):
        custo = 0
        for ing in self.ingredientereceita_set.all():
            custo += ing.ingrediente.preco * ing.quantidade
        return round(custo, 2)
    custo.short_description = 'Custo (R$)'

    def custo_por_rendimento(self):
        return self.custo() / Decimal(self.rendimento)
    custo_por_rendimento.short_description = "Custo por rendimento (R$)"

    def preco_sugerido(self):
        return round(self.custo() + (self.custo() * Decimal(0.3)),2)
    preco_sugerido.short_description = 'Preço Sugerido (R$)'

    def preco_sugerido_por_rendimento(self):
        return round(self.custo_por_rendimento() + (self.custo_por_rendimento() * Decimal(0.3)),2)
    preco_sugerido_por_rendimento.short_description = "Preço sugerido por rendimento"

    def __str__(self):
        return self.produto.nome

    class Meta:
        ordering = ('produto__nome',)


class Unidade(models.Model):
    nome = models.CharField(max_length=10)

    def __str__(self):
        return self.nome


class Ingrediente(models.Model):
    nome = models.CharField(max_length=200)
    unidade = models.ForeignKey(Unidade)
    preco = models.DecimalField('Preço', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome


class IngredienteReceita(models.Model):
    ingrediente = models.ForeignKey(Ingrediente)
    receita = models.ForeignKey(Receita)
    quantidade = models.DecimalField(max_digits=8, decimal_places=2)
