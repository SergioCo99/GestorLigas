# Generated by Django 3.1.1 on 2021-11-29 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0007_liga_imagen_liga'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liga',
            name='imagen_liga',
            field=models.ImageField(blank=True, default='default.png', upload_to='static/image/liga/'),
        ),
    ]
