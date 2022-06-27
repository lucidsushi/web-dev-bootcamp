from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import RoomSerializer, CreateRoomSerializer, UpdateRoomSerializer
from .models import Room

# Create your views (endpoints) here.
# Django server auto reloads the code when you save views

# from django.http import HttpResponse
# def main(request):
#     # return render(request, 'main.html')
#     return HttpResponse("<h1>Hello, world.</h1>")

# https://www.django-rest-framework.org/api-guide/generic-views/#generic-views


class AllRooms(generics.ListAPIView):
    '''Class-based view'''

    queryset = Room.objects.all()  # get all rooms
    serializer_class = RoomSerializer  # use to serialize data


class JoinRoom(APIView):
    """Associates the roomcode with the session
    (so we know user has joined the room before)
    """

    lookup_url_kwarg = 'code'  # does this have to be code??..

    def post(self, request):
        create_session_if_missing(self)
        code = request.data.get(self.lookup_url_kwarg)
        if not code:
            res = Response(
                {'Bad Request': f'POST data missing the key: {self.lookup_url_kwarg}'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        elif code and not len(Room.objects.filter(code=code)):
            # room_result = Room.objects.filter(code=code)
            # if not len(room_result):
            res = Response(
                {'Bad Request': f'Room Code: {code} does not exist'},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            # room = room_result[0]
            self.request.session['room_code'] = code
            res = Response(
                {'message': f'Successfully joined room: {code}'},
                status=status.HTTP_200_OK,
            )

        return res


class GetRoom(APIView):
    """
    - Also shows if the user is also the host of the room
    - Can have a session key without a session?
    """

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
                status=status.HTTP_404_NOT_FOUND,
            )
        else:
            return Response(
                {
                    'Bad Request': f'Parameter {self.lookup_url_kwarg} is not found in request'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class CreateRoomView(APIView):
    '''
    1. does session exist
    2. does room exist -- create
    3. return reponse
    4. associates the roomcode with the session,
       as user also "joins" the room on creation
      (so we know user has joined the room before)
    '''

    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        create_session_if_missing(self)
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
                self.request.session['room_code'] = room.code
                res = Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
            elif not queryset_exists:
                room = Room(
                    host=host,
                    guest_can_pause=guest_can_pause,
                    votes_to_skip=votes_to_skip,
                )
                room.save()
                self.request.session['room_code'] = room.code
                res = Response(RoomSerializer(room).data, status=status.HTTP_201_CREATED)
            else:
                res = Response(
                    {'Bad Request': 'Invalid data...'},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return res


class UserInRoom(APIView):
    def get(self, request, format=None):
        create_session_if_missing(self)
        # if a session is missing, how does a newly created session have the key 'room_code'?
        data = {'code': self.request.session.get('room_code')}
        # does not need rest framework object/serializer therefore use django response?
        return JsonResponse(data, status=status.HTTP_200_OK)


class LeaveRoom(APIView):
    """
    - Removes room_code from active Session
    - Delete room if host leaves
    """

    def post(self, request, format=None):
        if 'room_code' in self.request.session:
            self.request.session.pop('room_code')
            host_id = self.request.session.session_key
            room_results = Room.objects.filter(host=host_id)
            host_is_leaving = len(room_results) > 0
            if host_is_leaving:
                room = room_results[0]
                room.delete()

        return Response(
            {'message': 'leave-room end point successfully called'},
            status=status.HTTP_200_OK,
        )


class UpdateRoom(APIView):
    serializer_class = UpdateRoomSerializer

    def patch(self, request, format=None):
        create_session_if_missing(self)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            room_code = serializer.data.get('code')
            queryset = Room.objects.filter(code=room_code)
            if not queryset.exists():
                res = Response(
                    {'msg': f'Room {room_code} not found.'}, status=status.HTTP_404_NOT_FOUND
                )
            else:
                room = queryset[0]
                user_id = self.request.session.session_key
                if room.host != user_id:
                    res = Response(
                        {'Forbidden': 'You are not the host of this room.'},
                        status=status.HTTP_403_FORBIDDEN,
                    )
                else:
                    room.guest_can_pause = serializer.data.get('guest_can_pause')
                    room.votes_to_skip = serializer.data.get('votes_to_skip')
                    room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                    res = Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
        else:
            res = Response(
                {'Bad Request': "Invalid Data..."}, status=status.HTTP_400_BAD_REQUEST
            )

        return res


def create_session_if_missing(api_view):
    if api_view.request.session.exists(api_view.request.session.session_key):
        return
    else:
        api_view.request.session.create()
