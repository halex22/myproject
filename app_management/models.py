from django.db import models
from django.utils import timezone
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

class Artist(models.Model):
    """
    The model of an artist to be added to the database
    params when using form: name, genre fundation_date
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

    def __str__(self):
        return self.name

class Album(models.Model):
    """
    the model of an album to be added to the database
    params when using form: name, released_date, artist
    """
    name = models.CharField(max_length=50)
    released_date = models.DateField()
    added_date = models.DateField(default=timezone.now)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    
    def __str__(self) -> str:
        return self.name

@receiver(models.signals.pre_save, sender=Artist)
def artist_pre_save(sender, instance, **kwargs):
    instance.name = instance.name.lower()
    instance.genre = instance.genre.lower()

@receiver(models.signals.pre_save, sender=Album)
def album_pre_save(sender, instance, **kwargs):
    instance.name = instance.name.lower()