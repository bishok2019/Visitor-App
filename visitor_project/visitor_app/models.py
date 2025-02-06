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
    name = models.CharField(max_length=150)
    visiting_to = models.ForeignKey(Host,on_delete=models.CASCADE,related_name='host')
    meeting_date = models.DateField()
    meeting_time = models.TimeField()
    reason = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name