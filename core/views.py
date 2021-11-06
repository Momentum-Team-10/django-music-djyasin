from django.shortcuts import render, redirect, get_object_or_404
from .models import Album


def album_list(request):
    albums = Album.objects.all()
    return render(request, "templates/album_list.html",
                  {"albums": albums})


