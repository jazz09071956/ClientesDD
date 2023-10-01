# Generated by Django 4.2.5 on 2023-09-20 09:23

import client_sales.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_sales', '0002_sucursal_codigo_sucursal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventas_a_cliente',
            name='documento_venta',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='ventas_a_cliente',
            name='fecha_venta',
            field=models.DateField(default=client_sales.models.hoy),
        ),
    ]
