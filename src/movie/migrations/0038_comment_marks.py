# Generated by Django 3.2.15 on 2022-11-27 18:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movie', '0037_comment_who_has_it_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='marks',
            field=models.ManyToManyField(related_name='comnent_mark', to=settings.AUTH_USER_MODEL),
        ),
    ]
