from django.shortcuts import render


def chat_window(request, room_code):
    return render(request, template_name='chat_window.html', context={'room_code': room_code})