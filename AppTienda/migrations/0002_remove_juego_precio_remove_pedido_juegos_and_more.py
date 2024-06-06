# Generated by Django 5.0.6 on 2024-06-06 03:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppTienda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='juego',
            name='precio',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='juegos',
        ),
        migrations.AddField(
            model_name='juego',
            name='edad_recomendada',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='juego',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='AppTienda.juego'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]