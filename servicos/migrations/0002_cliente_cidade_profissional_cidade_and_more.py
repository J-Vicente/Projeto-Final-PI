# Generated by Django 4.2.3 on 2023-12-02 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(default='SOME STRING', max_length=150),
        ),
        migrations.AddField(
            model_name='profissional',
            name='cidade',
            field=models.CharField(default='Cidade', max_length=150),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cep',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=models.CharField(max_length=14),
        ),
    ]
