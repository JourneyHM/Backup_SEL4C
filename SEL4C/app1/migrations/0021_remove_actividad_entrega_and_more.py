# Generated by Django 4.2.4 on 2023-10-06 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_remove_administrador_progreso'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='entrega',
        ),
        migrations.RemoveField(
            model_name='progreso',
            name='autodiagnostico',
        ),
        migrations.AddField(
            model_name='progreso',
            name='completado',
            field=models.BooleanField(default=False, verbose_name='¿Completado?'),
        ),
        migrations.AddField(
            model_name='progreso',
            name='entrega',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.entrega', unique=True),
        ),
    ]
