from django.db import models

# Create your models here.


class Rooms (models.Model):
    room = models.CharField(max_length=255)
    sender = models.ForeignKey("Patient.Patient", related_name="Right", on_delete=models.CASCADE)
    receiver = models.ForeignKey("Patient.Patient", related_name="Left", on_delete=models.CASCADE)

class Messages (models.Model):
    room_name = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    sender = models.ForeignKey("Patient.Patient", on_delete=models.CASCADE)
    content = models.TextField()
    