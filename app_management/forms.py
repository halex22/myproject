from django.forms import Form, TextInput
from django.forms import CharField, IntegerField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.validators import MinLengthValidator, MaxLengthValidator
from datetime import datetime

class ArtistForm(Form):
    artist_name = CharField(label= "artist name",validators=[
        MinLengthValidator(limit_value=2, message="Name is too short"),
        MaxLengthValidator(limit_value=50,  message="Name is too long")
    ], widget=TextInput(attrs={"class":"input"}))
    genre = CharField(max_length=25, widget=TextInput(attrs={"class":"input"}))
    fundation_date = IntegerField(validators=[
        MinValueValidator(limit_value=1950, message="No artist before 1950"),
        MaxValueValidator(
        limit_value=datetime.now().year,
        message=f"Can't enter a higher than the current year"
    )], widget=TextInput(attrs={"class":"input"}))
    
class AlbumForm(Form):
    pass