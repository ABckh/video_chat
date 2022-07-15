from pip import main
from . import views
from django.urls import path

urlpatterns = [
    path('', views.connection, name='hello')
]


