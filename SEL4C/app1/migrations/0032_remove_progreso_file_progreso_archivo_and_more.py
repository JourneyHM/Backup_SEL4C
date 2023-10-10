# Generated by Django 4.2.6 on 2023-10-10 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0031_merge_20231009_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progreso',
            name='file',
        ),
        migrations.AddField(
            model_name='progreso',
            name='archivo',
            field=models.FileField(default='', upload_to='', verbose_name='Archivo'),
        ),
        migrations.AlterField(
            model_name='progreso',
            name='filename',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre de archivo'),
        ),
    ]
