from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import date


# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length=100, blank=False)
    nickname = models.CharField(max_length=100, blank=False)
    birthday = models.DateField(default=date(2000, 1, 1), blank=False)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
