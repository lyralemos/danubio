# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-04 23:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientereceita',
            name='quantidade',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
