# Generated by Django 4.0.6 on 2022-07-23 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connection', '0010_rename_link_channel_room_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='room_code',
            new_name='link',
        ),
    ]
