# Generated by Django 3.1.4 on 2020-12-07 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyeccion',
            name='time',
            field=models.TimeField(),
        ),
    ]