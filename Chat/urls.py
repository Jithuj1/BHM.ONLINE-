from django.urls import path, include

from .views import addRoom

urlpatterns = [
    path('add_room', addRoom)
]
