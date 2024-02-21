from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


# Create your models here.
class Account(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    username = models.CharField(max_length=150, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    is_superuser = models.BooleanField(default=False)
