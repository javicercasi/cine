# Generated by Django 3.1.1 on 2020-10-10 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[        # Codigo que va a generar el sql para contruir la tabla DB
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('duration', models.IntegerField()),
                ('description', models.CharField(default=False, max_length=200)),
                ('detail', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=30)),
                ('classification', models.CharField(max_length=5)),
                ('status', models.CharField(max_length=15)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Proyeccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('time', models.DateTimeField()),
                ('status', models.CharField(max_length=10)),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.pelicula')),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('status', models.CharField(max_length=15)),
                ('row', models.IntegerField()),
                ('seat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_r', models.DateTimeField()),
                ('row', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('proyeccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.proyeccion')),
            ],
        ),
        migrations.AddField(
            model_name='proyeccion',
            name='sala',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.sala'),
        ),
    ]
