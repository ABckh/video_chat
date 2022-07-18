from django.shortcuts import redirect, render
import re
from forms import UserRegisterForm, UserAuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def start_page(request):
    if request.user.is_authenticated:
        return render(request, template_name='connection.html')
    else:
        return redirect('registration')


def registration(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registration Successful!"))
            return redirect('start_page')
    else:    
        form = UserRegisterForm()
    return render(request, template_name='registration.html', context={'form': form })


def authentication(request):
    if request.method == "POST":
        form = UserAuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password= password)
        if user is not None:
            login(request, user)
            print('password is right')
            return redirect('start_page')
        else:
            print('password is not right')  
            return render(request, template_name='login.html', context= {'form': UserAuthenticationForm, 
            'message': 'Username or password is not right'})
    else:
        form = UserAuthenticationForm()
    return render(request, template_name='login.html', context={'form': form})
    

def logout_view(request):
    logout(request)
    return redirect('start_page')


def connection_to_room(request):
    if request.POST:
        data = request.POST.dict()
        if bool(re.fullmatch(r"http://localhost/[a-z]{3}-[a-z]{4}-[a-z]{3}/", data['room_code'])):
            # room_code is existed 
            # connection to room (redirect to the /meet/room_name)
            context = {
                'room_code': data['room_code'],
            }
            return render(request=request, template_name="room.html", context=context)

        else:
            # return error 
            return render(request=request, template_name="connection.html", context={'error': 'Please, enter a valid meeting-link'})
    else:
        # if request.method is GET, then just redirect to start_page
        return redirect('start_page')