# Generated by Django 4.0.6 on 2022-07-19 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connection', '0002_alter_channel_connected_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='connected_users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
