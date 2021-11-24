# Generated by Django 3.2.9 on 2021-11-16 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('nombre', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=1000)),
                ('fecha_creacion', models.DateField()),
                ('liga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.liga')),
            ],
        ),
    ]