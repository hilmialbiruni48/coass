from django.db import models
from django.contrib.auth.models import User

class makanMinum(models.Model):

    #tanggal
    tanggal = models.CharField(max_length=30)

    #Jadwal Makan
    jadwalMakan = models.TimeField(blank=True, null=True)

    #Makan
    makan = models.CharField(max_length=30)

    #Minum
    minum = models.CharField(max_length=30)

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)

