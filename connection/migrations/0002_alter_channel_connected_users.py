# Generated by Django 4.0.6 on 2022-07-19 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('connection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='connected_users',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
