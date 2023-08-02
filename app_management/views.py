from typing import Any
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic.edit import CreateView
from .forms import ArtistForm, AlbumForm, NewForm
from .models import Artist, Album


def home(request):
    return render(request, "index.html")

class AddArtist(View):

    def __init__(self, **kwargs: Any):
        super().__init__(**kwargs)
        self.tp = "add_artist.html"
        self.form = ArtistForm
        self.artist = Artist

    def create_new_entry(self, cleaned_data) -> object:
        artist = self.artist(
            name=cleaned_data["artist_name"],
            genre=cleaned_data["genre"],
            fundation_date=cleaned_data["fundation_date"]
        )
        return artist

    def get(self, request):
        return render(request, self.tp, {"form":self.form()})
    
    def post(self, request):
        form = self.form(request.POST)
        print(self.form)
        if form.is_valid():
            new_artist = self.create_new_entry(form.cleaned_data)
            return HttpResponse("<h1>Well done</h1>")


class AddAlbum(View):

    def get(self, request):
        form = AlbumForm()
        return render(request, "add_album.html", {"form": form})
    
    def post(self, request):
        form = AlbumForm(request.POST)
        if form.is_valid():
            return HttpResponse("<h1>Well done</h1>")
        

class NewAlbumView(CreateView):
    template_name = "add_album.html"
    form_class = NewForm
    model = Album

    def get_success_url(self):
        pass