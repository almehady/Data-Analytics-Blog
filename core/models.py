from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Profile(AbstractUser):
    full_name = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    profile = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    ref_code = models.CharField(max_length=14, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)