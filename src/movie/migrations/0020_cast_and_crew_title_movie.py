# Generated by Django 4.1.2 on 2022-11-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0019_movie_cast_and_crew'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast_and_crew',
            name='title_movie',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]