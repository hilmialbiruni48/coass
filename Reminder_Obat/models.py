from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Medicine(models.Model):
    hari = models.CharField(max_length=30)
    due_time = models.TimeField(null=True, blank=True)
    time_now = models.DateTimeField(auto_now_add=True)
    obat = models.CharField(max_length=30)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 

