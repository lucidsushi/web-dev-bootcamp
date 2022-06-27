"""api.urls URL Configuration
"""
from django.urls import path
from .views import (
    AllRooms, CreateRoomView, GetRoom, JoinRoom, UserInRoom, LeaveRoom, UpdateRoom
)

urlpatterns = [
    path('room', AllRooms.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('join-room', JoinRoom.as_view()),
    path('user-in-room', UserInRoom.as_view()),
    path('leave-room', LeaveRoom.as_view()),
    path('update-room', UpdateRoom.as_view())
]
