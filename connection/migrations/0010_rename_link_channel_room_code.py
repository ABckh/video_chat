# Generated by Django 4.0.6 on 2022-07-23 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0009_remove_channel_channel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='link',
            new_name='room_code',
        ),
    ]
