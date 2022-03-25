from datetime import datetime
from django.db import models

class Account(models.Model):
    login = models.CharField(max_length=70, default='')
    status = models.CharField(max_length=70, default='')
    created_at = models.DateTimeField(default=datetime.now, null=True, blank=True, editable=False)



