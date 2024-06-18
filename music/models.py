from django.db import models

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=100)



    def __str_(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, related_name="songs", on_delete=models.CASCADE)
    artist = models.CharField(max_length=150)
    title = models.CharField(max_length=200)
    duration = models.DurationField()


    def __str__(self) -> str:
        return self.title