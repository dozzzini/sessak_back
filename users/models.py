from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    nickname = models.CharField(max_length=10)
    location = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.nickname} ({self.location})"
