from django.db import models
from django.conf import settings

from .hash_id import generate_hash_id
from mixins import ModelStrMixin


class Category(ModelStrMixin, models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        default=generate_hash_id,
        editable=False
    )
    name = models.CharField(max_length=255)


class Task(ModelStrMixin, models.Model):
    id = models.CharField(
        primary_key=True,
        max_length=64,
        default=generate_hash_id,
        editable=False
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
