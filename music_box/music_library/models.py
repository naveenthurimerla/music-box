from django.db import models

from datetime import datetime


class Language(models.Model):
    '''
    This class used to hold the languages information   
    '''
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
        indexes = [
            models.Index(fields=['name'], name='idx_language_name'),
        ]

    def __str__(self):
        '''
        return the holding languages information
        '''
        return self.name


class Company(models.Model):
    '''
    This class is used to store the music company information
    '''
    name = models.CharField(max_length=200)
    logo = models.URLField(null=True)
    website = models.URLField(max_length=200, null=True)
    about = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        indexes = [
            models.Index(fields=['name'], name='idx_company_name'),
        ]

    def __str__(self):
        '''
        Return the holding music company information
        '''
        return self.name


class Artist(models.Model):
    '''
    This class is used to store the artist information like music composer, 
    
    singer, lyricist, actor and actress etc
    '''
    name = models.CharField(max_length=200)
    rating = models.IntegerField(default=0)
    image = models.URLField(null=True)
    about = models.URLField(null=True)

    class Meta:
        verbose_name = "Artist"
        verbose_name_plural = "Artists"
        indexes = [
            models.Index(fields=['name'], name='idx_artist_name'),
        ]

    def __str__(self):
        '''
        return the holding artist name 
        '''
        return self.name


class Genre(models.Model):
    '''
    This class used to hold the music genres information   
    '''
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"
        indexes = [
            models.Index(fields=['name'], name='idx_genre_name'),
        ]

    def __str__(self):
        '''
        return holding music genres information
        '''
        return self.name


class Album(models.Model):
    '''
    This class used to hold the albums information   
    '''
    name = models.CharField(max_length=200)
    composed_by = models.ManyToManyField(
        Artist)
    released_by = models.ManyToManyField(
        Company, related_name="album_released_by")
    genre = models.ForeignKey(
        Genre, on_delete=models.CASCADE)
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    cover = models.URLField(null=True)
    casting = models.ManyToManyField(Artist, related_name="album_casting")
    released_on = models.DateTimeField(default=datetime.now)
    added_on = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        indexes = [
            models.Index(fields=['name'], name='idx_album_name'),
        ]

    def __str__(self):
        '''
        returns holding the albums information   
        '''
        return self.name


class Track(models.Model):
    '''
    This class used to hold music track information   
    '''
    title = models.CharField(max_length=300)
    alt_title = models.CharField(max_length=300)
    artist = models.ManyToManyField(Artist)
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE)
    url = models.URLField(unique=True)
    rating = models.IntegerField(default=0)
    length = models.FloatField(default=0)
    added_on = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"
        indexes = [
            models.Index(fields=['title'],
                         name='idx_track_title'),
        ]

    def __str__(self):
        '''
        returns the holding music track information   
        '''
        return self.title


class Lyric(models.Model):
    '''
    This class used to hold the track lyrics information   
    '''
    track = models.ForeignKey(
        Track, on_delete=models.CASCADE)
    author = models.ManyToManyField(Artist)
    description = models.URLField(null=True)

    class Meta:
        verbose_name = "Lyric"
        verbose_name_plural = "Lyrics"

    def __str__(self):
        '''
        returns the holding track lyrics information   
        '''
        return self.track
