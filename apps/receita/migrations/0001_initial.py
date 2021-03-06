# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 23:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
            ],
        ),
        migrations.CreateModel(
            name='IngredienteReceita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
                ('ingrediente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receita.Ingrediente')),
            ],
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField(verbose_name='Descrição')),
                ('ingredientes', models.ManyToManyField(through='receita.IngredienteReceita', to='receita.Ingrediente')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Unidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='ingredientereceita',
            name='receita',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receita.Receita'),
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receita.Unidade'),
        ),
    ]
