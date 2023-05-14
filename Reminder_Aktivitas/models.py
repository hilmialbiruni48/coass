from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Activity(models.Model):
    date = models.CharField(max_length=30)
    aktivitas = models.TextField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

class Event(models.Model):
    tanggal = models.DateField()
    event = models.TextField()
    waktuawal = models.TimeField()
    waktuakhir = models.TimeField()

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    