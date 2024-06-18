from django.shortcuts import render
from .models import Album, Song

# Create your views here.


def albumlist(request):
    albums = Album.objects.all()
    return render(request, 'music/album_list.html', {"album":albums})



def songList(request):
    songs = Song.objects.all()
    return render(request, 'music/song_list.html', {"songs": songs})