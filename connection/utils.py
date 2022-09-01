from .models import Channel


def get_object_or_bool_channel(link):
    try:
        link = Channel.objects.get(link=link)
        return link.auto_delete
    except Channel.DoesNotExist:
        return False
