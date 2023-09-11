from django.db import models

# Create your models here.

class User(models.Model):
    nickname = models.CharField(max_length=10)
    location = models.CharField(max_length=30)

    def __str__(self) -> str:
        return f"{self.nickname} ({self.location})"