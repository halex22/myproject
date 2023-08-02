"""Django imports"""
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from app_management.models import Album, Artist

# Create your views here.
def home(request):
    return render(request, "myapp/index.html")

class AlbumsList(TemplateView):
    template_name = "myapp/album_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["albums"] = Album.objects.all()
        return context
    
class SingleAlbum(TemplateView):
    template_name = "myapp/album.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_album = Album.objects.get(pk=kwargs["id"])
        context["album"] = selected_album
        return context

class ArtistList(ListView):
    template_name = "myapp/artist_list.html"
    model = Artist
    context_object_name = "artists"

class SingleArtist(DetailView):
    template_name = "myapp/artist.html"
    model = Artist