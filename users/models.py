from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    email = models.EmailField()
    nickname = models.CharField(max_length=10)
    location = models.CharField(max_length=30)

    LOGIN_HOME = "home "
    LOGIN_GOOGLE = "google"
    LOGIN_CHOICES = (
        (LOGIN_HOME, "home"),
        (LOGIN_GOOGLE, "google"),
    )

    USERNAME_FIELD = "email"

    login_method = models.CharField(
        max_length=8, choices=LOGIN_CHOICES, default=LOGIN_HOME
    )

    def __str__(self) -> str:
        return f"{self.nickname} ({self.location})"
