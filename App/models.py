from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Song(models.Model):
    # song_id=models.AutoField()
    title = models.TextField(default="")
    artist = models.TextField(default="")
    image = models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    duration = models.CharField(max_length=20,default="0")
    release_date = models.DateField(default=timezone.now())
    paginate_by = 2
    def __str__(self):
        return self.title

class Category(models.Model):
    # id=models.AutoField()
    name = models.TextField()
    public = models.BooleanField(default=False)
    priority = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class Playlist(models.Model):
    # id = models.AutoField()
    name = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    songs = models.ManyToManyField(Song)
    image = models.ImageField(default="trying-album-cover.jpg")
    def __str__(self):
        return self.name
    
class UserSong(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    song = models.ForeignKey(Song,on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    no_of_times_played = models.IntegerField(default=0)
    last_time_played = models.DateTimeField()
    class Meta:
        unique_together = ('user','song',)
    def __str__(self):
        return self.user.username+"_"+self.song.title
