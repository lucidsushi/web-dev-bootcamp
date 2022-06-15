"""api.urls URL Configuration
"""
from django.urls import path
from .views import AllRooms, CreateRoomView, GetRoom

urlpatterns = [
    path('room', AllRooms.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view())
]
