from django.db import models
from django.conf import settings


class Channel(models.Model):
    is_active = models.BooleanField(default=False)
    connected_users = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )

