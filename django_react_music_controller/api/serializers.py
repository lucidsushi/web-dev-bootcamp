from rest_framework import serializers
from .models import Room

# id fields auto comes with each model (not defined manually at Room)
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_slip', 'created_at')