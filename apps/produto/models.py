from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)
