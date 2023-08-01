from django.shortcuts import render
from .froms import ArtistForm


def home(request):
    return render(request, "index.html")


def add_artist(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            print("ok")
    else:
        form = ArtistForm()
    context = {"form": form}
    return render(request, "add_artist.html", context=context)