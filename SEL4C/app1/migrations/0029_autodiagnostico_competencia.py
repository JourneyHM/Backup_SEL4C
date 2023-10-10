# Generated by Django 4.2.4 on 2023-10-09 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0028_autodiagnostico_completada'),
    ]

    operations = [
        migrations.AddField(
            model_name='autodiagnostico',
            name='competencia',
            field=models.CharField(choices=[('Autocontrol', 'Autocontrol'), ('Liderazgo', 'Liderazgo'), ('Conciencia y valor social', 'Conciencia y valor social'), ('Innovación social y sostenibilidad financiera', 'Innovación social y sostenibilidad financiera')], default='Autocontrol', max_length=60, verbose_name='Competencia que evalúa'),
        ),
    ]