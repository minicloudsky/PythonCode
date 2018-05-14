from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass


class Profile(models.Model):
    nickname = models.CharField(max_length=50, blank=True)
    user = models.OneToOneField(User)