from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class swabRecord(models.Model):
    tanggal = models.DateField(default=datetime.now)
    hasil = models.CharField(max_length=30)
    ctValue = models.CharField(max_length=30)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 