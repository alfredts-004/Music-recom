from django.db import models

class RecommendedMusic(models.Model):
    
    track_name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    subgenre = models.CharField(max_length=50)
    length_seconds = models.IntegerField()
    artist_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)

    def __str__(self):
        return self.track_name
