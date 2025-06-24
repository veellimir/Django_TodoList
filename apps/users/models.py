from django.contrib.auth.models import AbstractUser
from django.db import models

from mixins import ModelStrMixin


class Users(ModelStrMixin, AbstractUser):
    telegram_id = models.BigIntegerField(
        null=True,
        blank=True,
        unique=True,
    )
