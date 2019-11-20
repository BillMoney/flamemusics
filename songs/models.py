from django.db import models
from django.utils import timezone

# Create your models here.

class Songs(models.Model):
    song_title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    logo = models.ImageField(default='default.jpg', upload_to="media/")
    file = models.FileField(upload_to="media/")
    description = models.TextField()
    date_published = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{} {}".format(self.artist, self.song_title)