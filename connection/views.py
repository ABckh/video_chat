from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

import re

from . import forms
from .models import Channel


def start_page(request):
    if request.user.is_authenticated:
        return render(request, template_name='connection.html')
    else:
        return redirect('registration')


def registration(request):
    if request.method == "POST":
        form = forms.UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('start_page')
    else:    
        form = forms.UserRegisterForm()
    return render(request, template_name='registration.html', context={'form': form })


def authentication(request):
    if request.method == "POST":
        form = forms.UserAuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password= password)
        if user is not None:
            login(request, user)
            print('password is right')
            return redirect('start_page')
        else:
            print('password is not right')  
            return render(request, template_name='login.html', context= {'form': forms.UserAuthenticationForm, 
            'message': 'Username or password is not right'})
    else:
        form = forms.UserAuthenticationForm()
    return render(request, template_name='login.html', context={'form': form})
    

def logout_view(request):
    logout(request)
    return redirect('start_page')


def connection_to_room(request):
    if request.POST:
        data = request.POST.dict()
        if bool(re.fullmatch(r"http://localhost/[a-z]{3}-[a-z]{4}-[a-z]{3}/", data['room_code'])):
            link = Channel.objects.get(link=data['room_code'])
            if not link.auto_delete:
                link.connected_users.add(request.user)
                link.save()
                context = {
                    'room_code': data['room_code'],
                }
                return render(request=request, template_name="room.html", context=context)
            else:
                return render(request=request, template_name="connection.html", context={'error': 'This link is expired'})
        else:
            return render(request=request, template_name="connection.html", context={'error': 'Please, enter a valid meeting-link'})
    else:
        return redirect('start_page')
# Add link disconnect, when user is disconnected


def adding_active_link(request):
    data = request.POST.dict()
    new_record = Channel(link=data['link'], )
    new_record.save()   
    return redirect('start_page')


