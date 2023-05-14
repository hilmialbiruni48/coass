from django.db import models
from django.contrib.auth.models import User

class healthRecord(models.Model):
    #hari
    hari = models.CharField(max_length=30)

    #tanggal
    tanggal = models.DateField()

    #Suhu
    suhu = models.CharField(max_length=30)

    #Sistolik
    sistolik = models.CharField(max_length=30)

    #Diastolik
    diastolik = models.CharField(max_length=30)

    #Detak Jantung
    jantung = models.CharField(max_length=30)

    #Saturasi
    saturasi = models.CharField(max_length=30)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)