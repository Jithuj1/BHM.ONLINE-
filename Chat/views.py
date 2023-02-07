from django.shortcuts import render
from .serializers import RoomSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Rooms, Messages


# Create your views here.


@api_view(['GET', 'POST'])
def addRoom(request):
    sender = request.data.get('sender')
    receiver = request.data.get('receiver')
    print(sender, receiver)
    serializer = RoomSerializer(data= request.data)
    if serializer.is_valid():
        try:
            room = Rooms.objects.get(sender = sender, receiver =receiver)
            return room
        except:
            print("ijijijjji", serializer.data)
            serializer.save()
    return Response(status= status.HTTP_200_OK)