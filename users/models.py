from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    name = models.CharField(max_length=20, blank=True)
    avatar = models.FileField(blank=True)
