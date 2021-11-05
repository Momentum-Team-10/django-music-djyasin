from django.shortcuts import render
from .models import Album


def album_list(request):
    album = Album.objects.all()
    return render(request, "album/list_album.html",
                  {"album": album})