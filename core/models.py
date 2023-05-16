from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
# Create your models here.

STATUS_CHOICES = (
    ('D', 'Draft'),
    ('P', 'Published'),
)

class Profile(AbstractUser):
    full_name = models.CharField(max_length=200, blank=True)
    company_name = models.CharField(max_length=200, blank=True, null=True)
    profile = models.ImageField(upload_to='profile_pic/', null=True, blank=True)
    ref_code = models.CharField(max_length=14, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=False)
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='P')
    # user = models.ForeignKey('Profile', blank=True, null=True, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
