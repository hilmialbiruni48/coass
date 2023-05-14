from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    hari = models.CharField(max_length=2)
    tanggal = models.DateField()
    is_demam = models.BooleanField("Demam", default=False)
    is_batuk = models.BooleanField("Batuk", default=False)
    is_kelelahan = models.BooleanField("Kelelahan", default=False)
    is_penciuman = models.BooleanField("Kehilangan Penciuman", default=False)
    curhat = models.CharField(max_length=100)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
