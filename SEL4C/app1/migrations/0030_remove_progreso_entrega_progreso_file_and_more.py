# Generated by Django 4.2.4 on 2023-10-09 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0029_autodiagnostico_competencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progreso',
            name='entrega',
        ),
        migrations.AddField(
            model_name='progreso',
            name='file',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Archivo'),
        ),
        migrations.AddField(
            model_name='progreso',
            name='filename',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Título'),
        ),
        migrations.DeleteModel(
            name='Entrega',
        ),
    ]
