from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView, View
from django.views.generic.edit import CreateView
from app_management.models import Album, Artist
from .models import Profile
from .forms import ProfileForm

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

class CreateProfile(CreateView):
    template_name = "myapp/sign_up.html"
    form_class = ProfileForm
    model = Profile
    success_url = "/home"
    
    def form_valid(self, form):
        profile = form.save(commit=False)
        if "profile_pic" in self.request.FILES:
            profile.profile_pic = self.request.FILES['profile_pic']
        profile.save()
        return super().form_valid(form)

class ProfileView(DetailView):
    template_name = "myapp/user_profile.html"
    model = Profile
    