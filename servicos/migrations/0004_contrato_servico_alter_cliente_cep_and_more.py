# Generated by Django 4.2.3 on 2023-12-03 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0003_alter_cliente_cidade_alter_profissional_cidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='servico',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='profissional',
            name='celular',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='profissional',
            name='cep',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='profissional',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]
