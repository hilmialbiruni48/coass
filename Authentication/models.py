from django.db import models

class Login(models.Model):
    #username
    username = models.CharField(max_length=30)

    #pass
    password = models.CharField(max_length=30)

    #pass valid
    passValid = models.CharField(max_length=30)


