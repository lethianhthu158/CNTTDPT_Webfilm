# Generated by Django 3.2.15 on 2022-11-28 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0043_award'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='Ep',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
