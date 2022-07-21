from . import views
from django.urls import path


urlpatterns = [
    path('<str:room_code>/', views.chat_window, name='chat_window')
]