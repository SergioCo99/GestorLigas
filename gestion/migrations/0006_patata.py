# Generated by Django 3.1.1 on 2021-11-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0005_auto_20211128_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patata',
            fields=[
                ('nombre_equip', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
    ]
