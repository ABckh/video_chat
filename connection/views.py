from django.shortcuts import render
from video_chat.settings import BASE_DIR

# Create your views here.


def connection(request):
    context = {
        'hello': 'world'
    }
    return render(request, template_name='connection.html', context=context)