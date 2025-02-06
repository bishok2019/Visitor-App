#models.py
from django.db import models
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150, unique=True)
    dep_code = models.CharField(max_length=120, unique=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractBaseUser, PermissionsMixin):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Visitor(models.Model):
    name = models.CharField(max_length=150)
    visiting_to = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='host')
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    reason = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name