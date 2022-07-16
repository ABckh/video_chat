from django.shortcuts import redirect, render
import re

def start_page(request):
    context = {
        'hello': 'world'
    }
    return render(request, template_name='connection.html', context=context)

def connection_to_room(request):
    if request.POST:
        data = request.POST.dict()
        if bool(re.fullmatch(r"https://localhost/[a-z]{3}-[a-z]{3}-[a-z]{3}/", data['room_code'])):
            # room_code is existed 
            # connection to room (redirect to the /meet/room_name)
            context = {
                'room_code': data['room_code'],
            }
            return render(request=request, template_name="room.html", context=context)

        else:
            context = {
                'error': 'Please, enter right meeting-link'
            }
            return render(request=request, template_name="connection.html", context=context)
    else:
        return redirect('start_page')