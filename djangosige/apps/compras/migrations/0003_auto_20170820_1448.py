# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-20 17:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_auto_20170625_1450'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orcamentocompra',
            options={'permissions': (('view_orcamentocompra', 'Can view orcamento compra'),), 'verbose_name': 'Orçamento de Compra'},
        ),
        migrations.AlterModelOptions(
            name='pedidocompra',
            options={'permissions': (('view_pedidocompra', 'Can view pedido compra'), ('faturar_pedidocompra', '你可以申请购买')), 'verbose_name': 'Pedido de Compra'},
        ),
    ]
