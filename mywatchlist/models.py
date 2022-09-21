from platform import release
from django.db import models

# Create your models here.
class WatchlistModel(models.Model):
    watched = models.CharField(max_length = 225)
    title = models.CharField(max_length = 225)
    rating = models.FloatField()
    release_date = models.CharField(max_length = 225)
    review = models.TextField()

