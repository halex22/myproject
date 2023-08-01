from django.shortcuts import render
from .forms import ArtistForm, AlbumForm
from .models import Artist


def home(request):
    return render(request, "index.html")


def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = Artist(
                name= form.cleaned_data["artist_name"],
                genre= form.cleaned_data["genre"],
                fundation_date= form.cleaned_data["fundation_date"]
            )
            artist.save()            
    else:
        form = ArtistForm()
    context = {"form": form}
    return render(request, "add_artist.html", context=context)

def add_album(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            print(form)
    else:
        form = AlbumForm()
    context = {"form": form}
    return render(request, "add_album.html", context=context)