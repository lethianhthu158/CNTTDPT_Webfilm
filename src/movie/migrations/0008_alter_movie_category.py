# Generated by Django 4.1.2 on 2022-11-19 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_movie_episodes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('A', 'ACTION'), ('D', 'DRAMA'), ('C', 'COMEDY'), ('R', 'ROMANCE')], max_length=2),
        ),
    ]
