from django.shortcuts import render
from .forms import ArtistForm
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