from django.shortcuts import render, redirect, get_object_or_404
from .models import Album
from .forms import AlbumForm


def album_list(request):
    albums = Album.objects.all()
    return render(request, "album_list.html",
                {"albums": albums})

def add_album(request):
    if request.method == "POST":
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()

            return redirect("album_list")
    else:
        form = AlbumForm()
    return render(request, "add_album.html", {"form": form})