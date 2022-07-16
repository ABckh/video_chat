from pip import main
from . import views
from django.urls import path

urlpatterns = [
    path('', views.start_page, name='start_page'),
    path('meeting/', views.connection_to_room, name='room_connection' )
]


