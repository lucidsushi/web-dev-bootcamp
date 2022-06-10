from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room

# Create your views (endpoints) here.
# Django server auto reloads the code when you save views

# from django.http import HttpResponse
# def main(request):
#     # return render(request, 'main.html')
#     return HttpResponse("<h1>Hello, world.</h1>")

# https://www.django-rest-framework.org/api-guide/generic-views/#generic-views


class RoomView(generics.ListAPIView):
    ''' Class-based view
    '''
    queryset = Room.objects.all()  # get all rooms
    serializer_class = RoomSerializer  # use to serialize data


class CreateRoomView(APIView):
    '''
    1. does session exist
    2. does room exist -- create
    3. return reponse
    '''
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        if not self.request.session.exists(self.request.session.session_key):
            self.request.session.create()
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
            return Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
