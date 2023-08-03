from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.home, name="home"),
    path("albums", view=views.AlbumsList.as_view(), name="albums"),
    path("album/<int:id>", view=views.SingleAlbum.as_view(), name="album"),
    path("artists", view=views.ArtistList.as_view(), name="artists"),
    path("artist/<int:pk>", view=views.SingleArtist.as_view(), name="artist"),
    path("sign-up", view=views.CreateProfile.as_view(), name="sign-up"),
    path("user-profile/<int:pk>", view=views.ProfileView.as_view(), name="user-profile")
]
