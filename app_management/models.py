from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Artist(models.Model):
    """
    The model of an artist to be added to the database
    """
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=25)
    added_date = models.DateField(default=timezone.now)
    fundation_date = models.IntegerField(validators=[
        MinValueValidator(
        limit_value=1950,
        message="No artist before 1950"
    ), MaxValueValidator(
        limit_value=datetime.now().year,
        message=f"Can't enter a higher than the current year"
    )
    ], null=True, blank=True)

    def __init__(self, name: str, genre: str, fundation_date: int ) -> None:
        self.name = name
        self.genre = genre
        self.fundation_date = fundation_date

    def __repr__(self) -> str:
        return f"{self.name}"

class Album(models.Model):
    name = models.CharField(max_length=50)
    released_date = models.DateField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"{self.name}"
