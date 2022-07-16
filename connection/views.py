from importlib.resources import contents
from django.shortcuts import render
from video_chat.settings import BASE_DIR

# Create your views here.


def start_page(request):
    context = {
        'hello': 'world'
    }
    return render(request, template_name='connection.html', context=context)

def connection_to_room(request):
    if request.POST:
        data = request.POST.dict()
        room_code = data['room_code']
        # room_code is valid
        # room_code is existed 
        # connection to room
    else:
        # generate unique room_code
        pass
    context = {
        'room_code': room_code,
    }
    return render(request=request, template_name="room.html", context=context)