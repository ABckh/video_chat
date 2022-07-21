from . import views
from django.urls import path

urlpatterns = [
    path('', views.start_page, name='start_page'),
    # change this url to meeting/<str:room_ 
    path('meeting/', views.connection_to_room, name='room_connection' ),
    path('registration/', views.registration, name='registration'),
    path('authentication/', views.authentication, name='authentication'),
    path('logout/', views.logout_view, name='logout_view'),
    path('adding_active_link/', views.adding_active_link, name='adding_active_link'),

]


