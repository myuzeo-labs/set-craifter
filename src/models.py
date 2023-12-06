from django.db import models


class AudioTrack(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    artist = models.CharField(max_length=200, db_index=True)
    album = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    release_date = models.DateField()
    bpm = models.IntegerField()
    key = models.CharField(max_length=10)
    duration = models.FloatField()

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Playlist(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    tracks = models.ManyToManyField(AudioTrack)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.EmailField(max_length=100, unique=True, db_index=True)
    playlists = models.ManyToManyField(Playlist)

    def __str__(self):
        return self.username
