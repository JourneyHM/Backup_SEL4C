# Generated by Django 4.2.4 on 2023-08-31 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_remove_entrega_file_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='correo',
            field=models.EmailField(default='admin@example.com', max_length=50, unique=True, verbose_name='Correo'),
        ),
    ]
