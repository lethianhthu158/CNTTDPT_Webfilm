# Generated by Django 3.2.15 on 2022-11-26 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0032_alter_comment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='name',
        ),
    ]
