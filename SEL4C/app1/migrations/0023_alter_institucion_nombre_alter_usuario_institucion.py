# Generated by Django 4.2.6 on 2023-10-08 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_alter_institucion_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institucion',
            name='nombre',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Institución'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='institucion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.institucion'),
        ),
    ]
