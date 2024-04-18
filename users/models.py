from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birth_date = models.DateTimeField(
        blank=True,
        null=True,
    )
