from django.db import models
from django.conf import settings


# Create your models here.

class CoreMapping(models.Model):
    counter = models.IntegerField(default=settings.CORE_COUNTER_START)
    long_url = models.URLField(max_length=1024, null=False)
    short_url = models.URLField(max_length=128)

    def __str__(self):
        return self.short_url

    def save(self, *args, **kwargs):
        self.counter = self.counter + 1
        super().save(*args, **kwargs)
