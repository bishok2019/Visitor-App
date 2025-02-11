#models.py
from django.db import models
# Create your models here.
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from host_app.models import Host

# Create your models here.
class Visitor(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('checked_in', 'Checked-In'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    name = models.CharField(max_length=150)
    phone_num = models.CharField(max_length=15,null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    photo = models.ImageField(upload_to='visitor_photos/',null=True, blank=True)
    visiting_to = models.ForeignKey(Host,on_delete=models.CASCADE,related_name='host')
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    reason = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    def __str__(self):
        return self.name