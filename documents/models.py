import datetime

from django.db import models
from django.utils import timezone

class Document(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.title
