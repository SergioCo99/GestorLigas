# Generated by Django 3.1.1 on 2021-11-29 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0008_auto_20211129_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liga',
            name='imagen_liga',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
