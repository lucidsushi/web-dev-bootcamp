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


class AllRooms(generics.ListAPIView):
    ''' Class-based view
    '''
    queryset = Room.objects.all()  # get all rooms
    serializer_class = RoomSerializer  # use to serialize data


class GetRoom(APIView):
    serialier_class = RoomSerializer
    lookup_url_kwarg = 'code'  # does this have to be code??..

    def get(self, request, format=None):
        code = request.GET.get(self.lookup_url_kwarg)
        if code:
            room = Room.objects.filter(code=code)
            if len(room) > 0:
                data = RoomSerializer(room[0]).data
                data['is_host'] = self.request.session.session_key == room[0].host
                return Response(data, status=status.HTTP_200_OK)

            return Response(
                {f'Room Not Found: Invalid Room Code: {code}'},
                status=status.HTTP_404_NOT_FOUND
            )
        else:
            return Response(
                {'Bad Request': f'Parameter {self.lookup_url_kwarg} is not found in request'},
                status=status.HTTP_400_BAD_REQUEST
            )


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
            queryset_exists = queryset.exists()
            if queryset_exists:
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                res = Response(RoomSerializer(room).data,
                               status=status.HTTP_201_CREATED)
            elif not queryset_exists:
                room = Room(host=host, guest_can_pause=guest_can_pause,
                            votes_to_skip=votes_to_skip)
                room.save()
                res = Response(RoomSerializer(room).data,
                               status=status.HTTP_201_CREATED)
            else:
                res = Response({'Bad Request': 'Invalid data...'},
                               status=status.HTTP_400_BAD_REQUEST)
        return res
