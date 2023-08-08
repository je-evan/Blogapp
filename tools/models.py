from django.db import models
from django.utils import timezone


class Subscribe(models.Model):
    email = models.EmailField(max_length=50)
    date_submitted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email.split('@')[0]