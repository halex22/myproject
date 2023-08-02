from django.forms import Form, NumberInput, ModelForm
from django.forms.widgets import TextInput, Select, Input
from django.forms import CharField, IntegerField, ModelChoiceField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator
from datetime import datetime
from .models import Artist, Album

length_validatos = [MinLengthValidator(limit_value=2, message="Name is too short"),
                    MaxLengthValidator(limit_value=50, message="Name is too long")]


class ArtistForm(Form):
    artist_name = CharField(label="artist name", validators=length_validatos,
                            widget=TextInput(attrs={"class": "input"}))
    genre = CharField(max_length=25, widget=TextInput(attrs={"class": "input"}))
    fundation_date = IntegerField(validators=[
        MinValueValidator(limit_value=1950, message="No artist before 1950"),
        MaxValueValidator(
            limit_value=datetime.now().year,
            message=f"Can't enter a higher than the current year"
        )], widget=NumberInput(attrs={"class": "input"}))


class AlbumForm(Form):
    artist_choices = Artist.objects.all()
    album_name = CharField(label="Album name", validators=length_validatos, widget=TextInput(attrs={"class": "input"}))
    released_date = IntegerField(validators=[
        MinValueValidator(limit_value=1950, message="No artist before 1950"),
        MaxValueValidator(
            limit_value=datetime.now().year,
            message=f"Can't enter a higher than the current year"
        )], widget=NumberInput(attrs={"class": "input"}))
    artist = ModelChoiceField(label="Artist", queryset=artist_choices,
                              widget=Select(attrs={"class": "input"}))


class NewForm(ModelForm):
    class Meta:
        model = Album
        # fields = "__all__"
        exclude = ["added_date"]
        labels = {
            "name": "Name of the album"
        }
        widgets = {
            "name": TextInput(attrs={"class": "form-element"}),
            "released_date": Input(
                attrs={
                    "class": "form-element",
                    "type": "date"
                },
            ),
            "artist": Select(attrs={"class": "form-element artist"})
        }
        error_messages = {
            "album_name": {
                "required": "album name can not be empty"
            }
        }
