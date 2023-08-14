from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from .forms import NewForm, NewArtistForm
from .models import Artist, Album
from my_metal_code.decorators import show_errors, handle_img_from_form, update_session


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["msg"] = "This works !" # to add new context data
        return context
    

class NewAlbumView(CreateView):
    template_name = "add_album.html"
    form_class = NewForm
    model = Album
    success_url = "/app-management"

    @show_errors
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @handle_img_from_form
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)
   

class NewArtistView(CreateView):
    template_name = "add_artist.html"
    model = Artist
    form_class = NewArtistForm
    success_url = "/app-management"

    @show_errors
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)

    @handle_img_from_form
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)
  

class SessionUpdate(View):

    @update_session(session_name="fav_artists", query_name="artist_info")
    def post(self, request: HttpRequest , *args, **kwargs):
        return JsonResponse({"message": "Session data updated successfully."})
