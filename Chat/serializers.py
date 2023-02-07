from rest_framework import serializers
from .models import Rooms, Messages


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = "__all__"