# Generated by Django 4.1.3 on 2023-08-08 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_management', '0005_artist_subgenres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]