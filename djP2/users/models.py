from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    carrera = models.CharField(max_length=10)
    gender = models.CharField(max_length=15)

    def __str__(self):
        return f'{self.user.username} Profile'
