# Generated by Django 5.0.2 on 2024-03-13 02:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_convidado_checkbox_selecionado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convidado',
            name='checkbox_selecionado',
        ),
    ]
