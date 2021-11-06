from django.shortcuts import render
from .models import Album


def album_list(request):
    album = Album.objects.all()
    return render(request, "core/base.html",
                  {"album": album})