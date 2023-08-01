from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("add-artist", view=views.add_artist, name="add_artist"),
    path("add-album", view=views.add_album, name="add_album")
]
