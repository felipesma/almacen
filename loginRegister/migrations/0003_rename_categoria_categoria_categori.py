# Generated by Django 3.2.8 on 2021-10-23 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginRegister', '0002_auto_20211023_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='categoria',
            new_name='categori',
        ),
    ]