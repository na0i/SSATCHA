# Generated by Django 3.2.3 on 2021-05-21 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_alter_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(to='movies.Genre'),
        ),
    ]
