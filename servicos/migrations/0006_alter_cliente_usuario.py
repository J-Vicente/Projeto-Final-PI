# Generated by Django 4.2.3 on 2023-12-07 13:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('servicos', '0005_cliente_usuario_alter_cliente_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
