from django.db.models import Model, CharField, DateField, ImageField
from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.utils import timezone


class Profile(Model):
    """
    Profile model class
    Params: name and profile_pic
    """
    name = CharField(unique=True, blank=False, validators=[
        MinLengthValidator(
            limit_value=6,
            message="Username is too short, add at least %(limit_value)d characters"
        ), MaxLengthValidator(
            limit_value= 15,
            message="Username is too long, the limit is %(limit_value)d" \
            "the you provide has %(show_value)d characters"
        )
    ], max_length=15)
    sing_up_date = DateField(default=timezone.now)
    profile_pic = ImageField(upload_to="images")


