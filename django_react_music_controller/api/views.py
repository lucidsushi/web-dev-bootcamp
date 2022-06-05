from django.shortcuts import render
from rest_framework import generics

from .serializers import RoomSerializer
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
