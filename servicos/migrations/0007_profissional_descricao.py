# Generated by Django 4.2.3 on 2023-12-11 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0006_alter_cliente_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='profissional',
            name='descricao',
            field=models.TextField(default='descrição'),
        ),
    ]
