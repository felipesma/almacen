# Generated by Django 3.2.8 on 2021-10-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegister', '0004_rename_categori_categoria_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='pago',
            field=models.IntegerField(default=0),
        ),
    ]