from typing import Any, Dict
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView, View
from django.views.generic.edit import CreateView
from app_management.models import Album, Artist
from .forms import ProfileForm
from my_metal_code.db_helper import get_fav_artists
from django.contrib.auth.views import LoginView, LogoutView


class Home(TemplateView):
    template_name = "myapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        if "fav_artists" in self.request.session:
            context["fav_artists"] = get_fav_artists(self.request.session["fav_artists"])
        return context
    

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

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        artist = self.get_object() 
        if "fav_artists" in self.request.session:
            fav_artist = [int(_) for _ in self.request.session["fav_artists"]]
            context["is_favorite"] = artist.id in fav_artist
        context["user"] = self.request.user
        return context
    

class Login(LoginView):
    template_name = "myapp/registration/log_in.html"
    redirect_authenticated_user = True

    def get_redirect_url(self) -> str:
        return reverse_lazy("home")


class Logout(LogoutView):

    def get_redirect_url(self) -> str:
        return reverse_lazy("home")
    

class UserView(DetailView):
    pass
