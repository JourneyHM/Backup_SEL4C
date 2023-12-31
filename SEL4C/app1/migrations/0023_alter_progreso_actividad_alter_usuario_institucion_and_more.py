# Generated by Django 4.1 on 2023-10-08 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_alter_progreso_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='progreso',
            name='actividad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.actividad'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='institucion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.institucion'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='pais',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.pais'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Contraseña'),
        ),
    ]
