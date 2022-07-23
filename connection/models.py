from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime


class Channel(models.Model):
    link = models.CharField(max_length=35, unique=True)
    adding_time = models.DateTimeField(default=datetime.datetime.now, blank=True)
    connected_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    @property
    def auto_delete(self):
        # add connected 0 or 1
        if self.connected_users.count() == 0:
            if self.adding_time < datetime.datetime.now(self.adding_time.tzinfo)-datetime.timedelta(minutes=5):
                print('time is')
                link = Channel.objects.get(pk=self.pk)
                link.delete()
                return False
            else:
                return True
        else: 
            return True            
            
        
    