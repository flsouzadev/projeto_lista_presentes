# Generated by Django 5.0.2 on 2024-03-11 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_convidado_presente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convidado',
            name='presente',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
