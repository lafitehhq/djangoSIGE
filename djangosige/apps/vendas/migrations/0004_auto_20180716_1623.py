# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-16 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0003_auto_20180712_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='mod_frete',
            field=models.CharField(choices=[('0', '代表发行人'), ('1', '代表收货人/发件人'), ('2', '代表第三方'), ('9', '免运费')], default='9', max_length=1),
        ),
    ]
