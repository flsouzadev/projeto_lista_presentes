# Generated by Django 5.0.2 on 2024-03-11 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_convidado_presenca_alter_convidado_presente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convidado',
            name='presente',
            field=models.CharField(default='Não há presente', max_length=5),
        ),
    ]
