import cgi
from .models import Channel


def get_object_or_bool_channel(link):
    try:
        link = Channel.objects.get(link=link)
        print(link.auto_delete)
        return link.auto_delete
    except Channel.DoesNotExist:
        return False
