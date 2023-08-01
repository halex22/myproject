from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("add-artist", view=views.AddArtist.as_view(), name="add_artist"),
    path("add-album", view=views.AddAlbum.as_view(), name="add_album")
]
