from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.HomeView.as_view(), name="home-management"),
    path("add-artist", view=views.NewArtistView.as_view(), name="add_artist"),
    path("new-add-album", view=views.NewAlbumView.as_view(), name="new-album"),
    path("session-update", view=views.SessionUpdate.as_view(), name="session-update"),
    path("register", view=views.NewUserView.as_view(), name="register")
]
