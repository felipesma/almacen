# Generated by Django 3.2.8 on 2021-10-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegister', '0005_auto_20211023_1724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='pago',
            field=models.IntegerField(default=1),
        ),
    ]