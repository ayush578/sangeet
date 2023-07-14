from django.contrib import admin
from . models import Song,UserSong,Category,Playlist


# Register your models here.
admin.site.register(Song)
admin.site.register(Category)
admin.site.register(Playlist)
admin.site.register(UserSong)
