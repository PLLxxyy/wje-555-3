import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.constants import UserRole


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=16, choices=UserRole.choices, default=UserRole.TENANT)
    nickname = models.CharField(max_length=80, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    avatar = models.URLField(blank=True)
    idCardNo = models.CharField(max_length=32, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.role = UserRole.ADMIN
        super().save(*args, **kwargs)

