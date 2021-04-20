from django.db import models
import datetime
from django.utils import timezone


class Article(models.Model):
    heading = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.CharField(max_length=2000)

    def __str__(self):
        return self.heading

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
