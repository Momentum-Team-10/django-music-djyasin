from django.db import models
from django.utils import timezone


class Album(models.Model):

    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
   

    def created_at(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title